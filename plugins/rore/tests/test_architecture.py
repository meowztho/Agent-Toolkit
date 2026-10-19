import json, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class ArchitectureTests(unittest.TestCase):
    def test_three_active_skills(self):
        found=sorted(p.name for p in (ROOT/'skills').iterdir() if (p/'SKILL.md').exists())
        self.assertEqual(found,['rore-evidence-review','rore-orchestration','rore-reconstruction'])
    def test_user_facing_identity(self):
        p=json.loads((ROOT/'plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(p['name'],'rore')
        c=json.loads((ROOT/'.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        self.assertEqual(c['name'],p['name'])
        self.assertEqual(p['version'],c['version'])
        self.assertEqual(p['extensions']['com.openai']['interface']['displayName'],'RORE')
    def test_no_downstream_active_owner(self):
        text='\n'.join((ROOT/x).read_text(encoding='utf-8') for x in ['docs/SYSTEM_MAP.yaml','docs/CAPABILITY_GRAPH.yaml','docs/SYSTEM_INTEGRATION.yaml'])
        for term in ['CR_PRODUCT','CR_BUILD','CR_RELEASE','CAP_PRODUCT_DECISIONS','CAP_RELEASE_GATE']:
            self.assertNotIn(term,text)

    def test_domain_neutrality(self):
        active = '\n'.join(p.read_text(encoding='utf-8').lower() for p in ROOT.rglob('*.md'))
        self.assertNotIn('games are a primary rore target', active)
        self.assertNotIn('games are the primary rore target', active)
        vision=(ROOT/'docs/USER_VISION.md').read_text(encoding='utf-8').lower()
        self.assertIn('domain-neutral', vision)
        decision=(ROOT/'docs/DECISION_COMPENDIUM.md').read_text(encoding='utf-8').lower()
        self.assertIn('none is a primary target', decision)
