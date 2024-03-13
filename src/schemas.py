from datetime import datetime
from typing import List
from pydantic import BaseModel, Field


class TagIn(BaseModel):
    name: str = Field(max_length=25)


class TagOut(TagIn):
    id: int

    class Config:
        orm_mode = True


class NoteIn(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150)
    done: bool | None
    tags: List[int] | None


class NoteOut(NoteIn):
    id: int
    created_at: datetime
    tags: List[TagOut]

    class Config:
        orm_mode = True


class NoteStatusUpdate(BaseModel):
    done: bool
