from typing import Optional
from sqlmodel import SQLModel, Field


class RequestHistory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tickers: str
    start_time: str
    end_time: str
