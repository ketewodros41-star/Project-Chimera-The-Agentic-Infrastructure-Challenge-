import time
from .swarm import SwarmNode, Result

class JudgeService(SwarmNode):
    def __init__(self, node_id: str = "primary-judge"):
        super().__init__(node_id)

    def judge_loop(self):
        print(f"Judge {self.node_id} started. Polling for results...")
        while True:
            result = self.pop_result()
            if result:
                print(f"Judge {self.node_id} reviewing result for Task ID: {result.task_id}")
                
                # Confidence-based logic as per SRS NFR 1.1
                if result.confidence_score >= 0.90:
                    print(f"✅ [AUTO-APPROVE] Task {result.task_id} approved. Result: {result.output}")
                elif result.confidence_score >= 0.70:
                    print(f"⚠️ [HITL-ESC] Task {result.task_id} requires manual review (Confidence: {result.confidence_score})")
                else:
                    print(f"❌ [REJECT] Task {result.task_id} rejected. Confidence too low ({result.confidence_score}).")
                
                # In a full migration, this would update the GlobalState in Postgres/Weaviate
            else:
                time.sleep(1)

if __name__ == "__main__":
    judge = JudgeService()
    judge.judge_loop()
