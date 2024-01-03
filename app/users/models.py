from typing import List
from pydantic import BaseModel, ConfigDict, Field

class UserBase(BaseModel):
    username: str
    email: str
    full_name: str

class UserDisplay(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: str = Field(..., alias="_id")
    disabled: bool = False
    topics: List[str] = []
    questions: List[str] = []
    frequency: str = 7