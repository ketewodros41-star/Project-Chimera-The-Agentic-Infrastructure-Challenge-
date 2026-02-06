import time
from .swarm import SwarmNode, Result

class JudgeService(SwarmNode):
    def __init__(self, node_id: str = "primary-judge"):
        super().__init__(node_id)
        # Mock global state version for OCC check
        self.current_state_version = "2026-02-06T00:00:00Z" 

    def judge_loop(self):
        print(f"Judge {self.node_id} started. Polling for results...")
        while True:
            result = self.pop_result()
            if result:
                print(f"Judge {self.node_id} reviewing Result ID: {result.task_id}")
                
                # Dimension 2: Optimistic Concurrency Control (OCC)
                # Reject if result version is older than current state
                if result.state_version < self.current_state_version:
                    print(f"❌ [OCC_REJECT] Task {result.task_id} stale. Result version: {result.state_version} < Current: {self.current_state_version}")
                    continue

                # Dimension 5: Tiered Escalation (SRS §5.1)
                # Logic: >0.90 -> Auto, 0.70-0.90 -> HITL Queue, <0.70 -> Reject
                if result.confidence_score >= 0.90:
                    print(f"✅ [AUTO-APPROVE] Task {result.task_id} approved. Confidence: {result.confidence_score}")
                elif result.confidence_score >= 0.70:
                    print(f"⚠️ [HITL-ESC] Task {result.task_id} moved to Approval Queue (Confidence: {result.confidence_score})")
                else:
                    print(f"❌ [AUTO-REJECT] Task {result.task_id} rejected. Confidence: {result.confidence_score}")
            else:
                time.sleep(1)

if __name__ == "__main__":
    judge = JudgeService()
    judge.judge_loop()
