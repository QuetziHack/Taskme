from datetime import datetime, timezone
from pydantic import BaseModel, Field

def utc_now():
    return datetime.now(timezone.utc)

class Task(BaseModel):
    title: str
    description: str
    registered_at: datetime = Field(default_factory=utc_now)
    start_date: datetime | None = None
    finish_date: datetime | None = None
    tolerance: int

