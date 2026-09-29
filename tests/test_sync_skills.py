import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from sync_skills import ROOT, sync
from check_repo import validate


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / 'repo'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))

    def test_idempotent(self):
        manifest = self.root / 'configs/generated-skills.json'
        before = manifest.read_bytes()
        sync(self.root)
        self.assertEqual(before, manifest.read_bytes())
        sync(self.root, check=True)

    def test_profile_switch_preserves_unmanaged_files(self):
        extra = self.root / '.claude/skills/reportes-marketing/personal.txt'
        extra.write_text('keep')
        sync(self.root, 'full')
        self.assertTrue((self.root / '.agents/skills/n8n/SKILL.md').exists())
        sync(self.root, 'engineering')
        self.assertEqual(extra.read_text(), 'keep')
        self.assertFalse((self.root / '.claude/skills/reportes-marketing/SKILL.md').exists())
        self.assertIn('perfil engineering', validate(self.root))

    def test_source_change_detected_and_synchronized(self):
        source = self.root / 'skills/copy-marketing/SKILL.md'
        source.write_text(source.read_text() + '\nNueva regla.\n')
        with self.assertRaisesRegex(ValueError, 'desactualizadas'):
            sync(self.root, check=True)
        sync(self.root)
        self.assertEqual(source.read_bytes(), (self.root / '.agents/skills/copy-marketing/SKILL.md').read_bytes())

    def test_edited_copy_is_not_overwritten(self):
        target = self.root / '.agents/skills/copy-marketing/SKILL.md'
        target.write_text('local changes')
        with self.assertRaisesRegex(ValueError, 'Copia editada'):
            sync(self.root, 'full')
        self.assertEqual(target.read_text(), 'local changes')
        self.assertFalse((self.root / '.agents/skills/n8n/SKILL.md').exists())

    def test_unmanaged_collision_is_not_overwritten(self):
        target = self.root / '.agents/skills/n8n/SKILL.md'
        target.parent.mkdir(parents=True)
        target.write_text('mine')
        with self.assertRaisesRegex(ValueError, 'Colisión'):
            sync(self.root, 'full')
        self.assertEqual(target.read_text(), 'mine')

    def test_path_escape_is_rejected(self):
        path = self.root / 'configs/skills.json'
        config = json.loads(path.read_text())
        config['profiles']['escape'] = ['../../outside']
        path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, 'Nombre no permitido'):
            sync(self.root, 'escape')

    def test_manifest_escape_is_rejected(self):
        path = self.root / 'configs/generated-skills.json'
        manifest = json.loads(path.read_text())
        manifest['files']['README.md'] = 'bad'
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, 'Entrada de manifiesto'):
            sync(self.root)

    def test_symlink_is_rejected(self):
        target = self.root / '.agents/skills/copy-marketing/SKILL.md'
        target.unlink()
        target.symlink_to(self.root / 'README.md')
        with self.assertRaisesRegex(ValueError, 'Enlace simbólico'):
            sync(self.root)


if __name__ == '__main__':
    unittest.main()
