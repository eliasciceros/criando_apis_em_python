from typing import List
from datetime import datetime, timedelta

from consts.date_formats import YY_MM_DD


def post_process(data, tickers: List[str]) -> dict:
    """
        Post process results because of the way it has been organized.
        P.S.: this function was given by activity.
    """

    data.dropna(axis=1, inplace=True)
    result = dict({ticker: dict() for ticker in tickers})

    try:
        for key, value in data.to_dict().items():
            if isinstance(key, tuple):
                (action, ticker) = key
                result[ticker][action] = value
            else:
                result[tickers[0]][key] = value
    except ValueError as e:
        raise e

    return result


def get_one_week_ago_date():
    """ Return the formated date of seven days before today. """
    return (datetime.now() - timedelta(weeks=1)).strftime(YY_MM_DD)


def get_todays_date():
    """ Return the formated date of today. """
    return datetime.now().strftime(YY_MM_DD)
