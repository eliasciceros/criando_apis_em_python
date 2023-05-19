from typing import List, Optional
from pydantic import BaseModel

from utils.utils import get_one_week_ago_date, get_todays_date


class StockExchangePriceBody(BaseModel):
    """ Stock Exchange Price Body Model. """
    tickers: List[str]
    start_time: Optional[str] = get_one_week_ago_date()
    end_time: Optional[str] = get_todays_date()
