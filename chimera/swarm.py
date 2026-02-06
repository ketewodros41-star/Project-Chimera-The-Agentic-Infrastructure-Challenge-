from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field
import uuid
from datetime import datetime
import redis
import json

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    REVIEW = "review"
    COMPLETE = "complete"
    FAILED = "failed"

class TaskType(str, Enum):
    GENERATE_CONTENT = "generate_content"
    REPLY_COMMENT = "reply_comment"
    EXECUTE_TRANSACTION = "execute_transaction"
    RESEARCH = "research"

class Task(BaseModel):
    task_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    task_type: TaskType
    priority: str = "medium"
    context: Dict[str, Any] = Field(default_factory=dict)
    assigned_worker_id: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    status: TaskStatus = TaskStatus.PENDING

class Result(BaseModel):
    task_id: str
    worker_id: str
    output: Any
    confidence_score: float = 1.0
    status: str = "success"
    reasoning_trace: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)

class SwarmNode:
    def __init__(self, node_id: str, redis_host: str = "localhost", redis_port: int = 6379):
        self.node_id = node_id
        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.task_queue = "task_queue"
        self.review_queue = "review_queue"

    def push_task(self, task: Task):
        self.redis.lpush(self.task_queue, task.model_dump_json())

    def pop_task(self) -> Optional[Task]:
        data = self.redis.rpop(self.task_queue)
        if data:
            return Task.model_validate_json(data)
        return None

    def push_result(self, result: Result):
        self.redis.lpush(self.review_queue, result.model_dump_json())

    def pop_result(self) -> Optional[Result]:
        data = self.redis.rpop(self.review_queue)
        if data:
            return Result.model_validate_json(data)
        return None
