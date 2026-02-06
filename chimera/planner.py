import json
import os
from typing import List
from .swarm import SwarmNode, Task, TaskType

class PlannerService(SwarmNode):
    def __init__(self, node_id: str = "primary-planner"):
        super().__init__(node_id)

    def decompose_goal(self, goals_file: str):
        if not os.path.exists(goals_file):
            print(f"Goals file {goals_file} not found.")
            return

        with open(goals_file, "r") as f:
            goals_data = json.load(f)

        print(f"Planner {self.node_id} processing goal: {goals_data.get('goal')}")
        
        # Simple rule-based decomposition for the demo
        # In a real scenario, this would involve an LLM call
        tasks = []
        if "content" in goals_data.get("goal", "").lower():
            tasks.append(Task(task_type=TaskType.RESEARCH, context={"topic": "AI Trends"}))
            tasks.append(Task(task_type=TaskType.GENERATE_CONTENT, context={"topic": "AI Trends", "platform": "twitter"}))
        
        if "transaction" in goals_data.get("goal", "").lower() or "pay" in goals_data.get("goal", "").lower():
            tasks.append(Task(task_type=TaskType.EXECUTE_TRANSACTION, context={"amount": 1.0, "to": "0x123..."}, priority="high"))

        for task in tasks:
            print(f"Pushing task: {task.task_type} (ID: {task.task_id})")
            self.push_task(task)

if __name__ == "__main__":
    # Create a mock goals file for testing if it doesn't exist
    mock_goals = {"goal": "Research AI content and pay for compute"}
    with open("goals.json", "w") as f:
        json.dump(mock_goals, f)
        
    planner = PlannerService()
    planner.decompose_goal("goals.json")
