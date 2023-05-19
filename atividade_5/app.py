"""
    Construcao de uma API que busca valores de cotacoes de acoes na bolsa de
    valores e retorna para o usuario da API. As buscas sao salvas em um banco
    de dados.
        - fastapi como framework de criacao de API
        - sqlmodel como ORM

    Modo de utilizacao:
        - Inicie o ambiente e acesse o swagger no endereco:
            - "localhost:PortaEscolhida/docs"
        - Digite os tickets com uma lista de string.
            - Exemplo: tickers = ["SPY", "AAPL", "MSFT"]
        - Digite as datas no formato "YY-MM-DD"

    P.S.: para iniciar o ambiente, execute no terminal deste diretorio:
        - uvicorn app:app --port 8081 --reload
        - Se uvicorn não é reconhecido como comando interno, execute:
            - python -m uvicorn app:app --port 8081 --reload
"""
__author__ = "Elias Cícero Moreira Guedes"
__date__ = "02 de Outubro de 2021"
__credits__ = ["Igor Souza, ministrante do curso 'Criando APIs em Python'"]


import json
from fastapi import FastAPI, HTTPException
from sqlmodel import create_engine, SQLModel, Session
from os import path
import yfinance as yf

from consts.db_url import DB_URL
from models.request_history import RequestHistory
from models.stock_exchange_price_body import StockExchangePriceBody
from utils.utils import post_process


app = FastAPI()

engine = create_engine(DB_URL)

if not path.isfile(DB_URL):
    SQLModel.metadata.create_all(engine)


@app.post("/stockexchangeprice")
def retrieve_and_save_request(body: StockExchangePriceBody):
    # Store request in the db
    with Session(engine) as session:
        userRequest = RequestHistory(
            tickers=json.dumps(body.tickers),
            start_time=body.start_time or "",
            end_time=body.end_time or ""
        )

        session.add(userRequest)
        session.commit()

    # Get the stock exchanges data for the given tickers in given period
    data = yf.download(
        " ".join(body.tickers),
        start=body.start_time,
        end=body.end_time
    )

    try:
        result = post_process(data, tickers=body.tickers)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="There is no value to return."
        )
    except KeyError:
        raise HTTPException(
            status_code=500,
            detail='Try to write the tickers input separated with comma like'
            ' [TICKER1, TICKER2] and the time input in the YY-MM-DD format',
        )

    return result
