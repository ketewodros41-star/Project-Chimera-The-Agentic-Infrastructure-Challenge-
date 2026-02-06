import asyncio
import os
import json
from chimera.planner import PlannerService
from chimera.worker import WorkerService
from chimera.judge import JudgeService
from chimera.commerce import CommerceManager
from chimera.swarm import Task, TaskType

async def run_demo():
    print("🚀 Starting Project Chimera Day 3 Rescue Demo...")
    
    # 1. Initialize Services
    planner = PlannerService()
    worker = WorkerService("demo-worker")
    judge = JudgeService()
    commerce = CommerceManager()
    
    # 2. Setup Goal
    goal = {"goal": "Research AI content and pay for compute"}
    with open("goals.json", "w") as f:
        json.dump(goal, f)
    
    print("\n--- Phase 1: Planning ---")
    planner.decompose_goal("goals.json")
    
    print("\n--- Phase 2: Execution (Worker) ---")
    # We'll process only the first two tasks for the demo
    task1 = planner.pop_task()
    if task1:
        print(f"Worker processing: {task1.task_type}")
        # In a real loop, worker.work_loop would be running
        # Here we simulate the processing
        output = f"Completed {task1.task_type} with research data."
        from chimera.swarm import Result
        result1 = Result(task_id=task1.task_id, worker_id="demo-worker", output=output)
        planner.push_result(result1)
    
    print("\n--- Phase 3: Quality Gate (Judge) ---")
    result = planner.pop_result()
    if result:
        print(f"Judge reviewing task: {result.task_id}")
        if result.confidence_score >= 0.9:
            print(f"✅ [APPROVED] {result.output}")
    
    print("\n--- Phase 4: Agentic Commerce ---")
    balance = await commerce.get_wallet_balance()
    print(f"Current Wallet Balance: {balance} USDC")
    if balance > 10:
        success = await commerce.send_payment("0xAgentComputeNode", 5.0)
        if success:
            print("💰 Payment for compute resources executed successfully.")

    print("\n✅ Demo Complete: Project Chimera is back on schedule!")

if __name__ == "__main__":
    asyncio.run(run_demo())
