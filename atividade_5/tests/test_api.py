"""
    Arquivos de teste

    Modo de utilizacao:
        - Instale o pytest: pip install pytest
        - Tenha seus arquivos de teste nomeados da seguinte forma:
            - Iniciando com test_ ou terminando com _test
        - No terminal deste projeto, execute o comando
            - python -m pytest
"""

from app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_stockexchangeprice0one_ticker():
    tickers = ["AAPL"]
    response = client.post(
        url="/stockexchangeprice",
        json={
            "tickers": tickers,
            "start_time": "2021-09-26",
            "end_time": "2021-10-03"
        }
    )

    assert response.status_code == 200
    assert list(response.json().keys()) == tickers


def test_stockexchangeprice_two_tickers():
    tickers = [
        "AAPL",
        "SPY",
    ]

    response = client.post(
        url="/stockexchangeprice",
        json={
            "tickers": tickers,
            "start_time": "2021-09-26",
            "end_time": "2021-10-03"
        }
    )

    assert response.status_code == 200
    assert list(response.json().keys()) == tickers
