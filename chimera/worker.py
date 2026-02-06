import time
from .swarm import SwarmNode, Result, TaskStatus

class WorkerService(SwarmNode):
    def __init__(self, node_id: str):
        super().__init__(node_id)

    def work_loop(self):
        print(f"Worker {self.node_id} started. Polling for tasks...")
        while True:
            task = self.pop_task()
            if task:
                print(f"Worker {self.node_id} processing task: {task.task_type} (ID: {task.task_id})")
                
                # Update status
                task.status = TaskStatus.IN_PROGRESS
                
                # Mock execution
                time.sleep(1)
                
                output = f"Result of {task.task_type} for {task.context}"
                result = Result(
                    task_id=task.task_id,
                    worker_id=self.node_id,
                    output=output,
                    confidence_score=0.95,
                    reasoning_trace=f"Executed {task.task_type} logic successfully.",
                    # Dimension 2: Returning the state_version for OCC check
                    state_version=getattr(task, 'state_version', '1970-01-01T00:00:00Z')
                )
                
                print(f"Worker {self.node_id} pushing result for task: {task.task_id}")
                self.push_result(result)
            else:
                time.sleep(1)

if __name__ == "__main__":
    import sys
    worker_id = sys.argv[1] if len(sys.argv) > 1 else "worker-1"
    worker = WorkerService(worker_id)
    worker.work_loop()
