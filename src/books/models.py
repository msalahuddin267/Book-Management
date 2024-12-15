from sqlmodel import SQLModel
from datetime import datetime

class Book(SQLModel, table=True):
    id: int
    title: str
    author: str
    publisher: str
    publish_date: str
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime