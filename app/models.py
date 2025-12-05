from pydantic import BaseModel
from typing import Literal

class UserAction(BaseModel):
    user_id: int
    action: Literal["click", "scroll", "view"]
    page: str
    device: str
    timestamp: int
