import json
import os
import time
from typing import List, Dict
from .swarm import SwarmNode, Task, TaskType

class PlannerService(SwarmNode):
    def __init__(self, node_id: str = "primary-planner"):
        super().__init__(node_id)
        # Dimension 2: GlobalState with OCC state_version
        self.state_version = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        self.global_state = {
            "campaigns": {},
            "state_version": self.state_version
        }

    def decompose_goal(self, goals_file: str):
        if not os.path.exists(goals_file):
            print(f"Goals file {goals_file} not found.")
            return

        with open(goals_file, "r") as f:
            goals_data = json.load(f)

        print(f"Planner {self.node_id} processing goal at version {self.state_version}")
        
        tasks = []
        if "content" in goals_data.get("goal", "").lower():
            # Dimension 1: Passing state_version to tasks for OCC
            tasks.append(Task(
                task_type=TaskType.RESEARCH, 
                context={"topic": "AI Trends"},
                state_version=self.state_version
            ))
            tasks.append(Task(
                task_type=TaskType.GENERATE_CONTENT, 
                context={"topic": "AI Trends", "platform": "twitter"},
                state_version=self.state_version
            ))
        
        for task in tasks:
            print(f"Pushing task: {task.task_type} (ID: {task.task_id})")
            self.push_task(task)

if __name__ == "__main__":
    mock_goals = {"goal": "Research AI content"}
    with open("goals.json", "w") as f:
        json.dump(mock_goals, f)
        
    planner = PlannerService()
    planner.decompose_goal("goals.json")
