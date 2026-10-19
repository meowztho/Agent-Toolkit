import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

class EvidenceReviewTests(unittest.TestCase):
    def test_review_is_read_only_and_independent(self):
        t=(ROOT/'skills/rore-evidence-review/SKILL.md').read_text(encoding='utf-8').lower()
        for x in ['read-only','do not mutate','do not silently edit','later `rore-reconstruction` pass']:
            self.assertIn(x,t)
    def test_review_checks_context_pollution_and_fidelity(self):
        t=(ROOT/'skills/rore-evidence-review/SKILL.md').read_text(encoding='utf-8').lower()
        self.assertIn('rejected hypotheses',t)
        self.assertIn('reference-native fidelity',t)
    def test_review_freshness_and_anti_anchoring(self):
        t=(ROOT/'skills/rore-evidence-review/SKILL.md').read_text(encoding='utf-8').lower()
        for x in ['fresh reviewer context','reconstruction-agent confidence','prior review conclusions','independently derived']:
            self.assertIn(x,t)
