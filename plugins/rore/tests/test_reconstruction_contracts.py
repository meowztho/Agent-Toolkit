import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def r(p): return (ROOT/p).read_text(encoding='utf-8')

class ReconstructionContractTests(unittest.TestCase):
    def test_reference_native_not_builder_normalized(self):
        t=r('skills/rore-reconstruction/SKILL.md').lower()
        self.assertIn('do not redesign',t)
        self.assertIn("reference's own structure",t)
    def test_decision_quality(self):
        o=r('skills/rore-orchestration/SKILL.md')+r('skills/rore-orchestration/references/ROUTING_AND_REPLAN.md')
        for x in ['continue | switch | stop','Negative Evidence','replan','bias']:
            self.assertIn(x,o)
    def test_perturbation_is_epistemic(self):
        t=r('skills/rore-reconstruction/references/PERTURBATION_AND_CAUSAL_PROBING.md').lower()
        self.assertIn('mechanism',t)
        self.assertIn('sufficient mechanism understanding',t)
        self.assertIn('do not continue into exploit stabilization',t)
    def test_runtime_ladder(self):
        t=r('skills/rore-reconstruction/references/RUNTIME_DYNAMIC_RECONSTRUCTION.md')
        self.assertIn('PRESENT → REFERENCED → REACHABLE → EXERCISED → EFFECTIVE',t)
    def test_visual_values_not_normalized(self):
        t=r('skills/rore-reconstruction/references/VISUAL_INTERACTION_RECONSTRUCTION.md')
        self.assertIn('Do not snap measured values',t)
    def test_current_state_liveness_guard(self):
        t=r('skills/rore-reconstruction/references/EVIDENCE_QUALIFICATION.md').lower()
        for x in ['current-state liveness','newly acquired artifact','stale, frozen, cached, replayed or disconnected','identical samples alone']:
            self.assertIn(x,t)
    def test_low_level_descent_is_information_driven(self):
        t=r('skills/rore-reconstruction/references/STATIC_CODE_BINARY_RECONSTRUCTION.md').lower()
        for x in ['decompiler / ir','bytecode / assembly','raw bytes / hex','live memory / machine state','do not descend for ceremony','stable semantic anchors']:
            self.assertIn(x,t)
