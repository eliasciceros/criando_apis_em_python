from typing import Dict, List
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from detection import DetectFace
from utils import base64_to_nparray

app = FastAPI()


class Body(BaseModel):
    # String em base64
    img: str


# Endpoint home
@app.get(path="/")
def hello_world() -> Dict[str, str]:
    return {"msg": "hello world"}


# Endpoint /time
@app.get(path="/time")
def time() -> Dict[str, datetime]:
    return {"msg": datetime.now()}


# Endpoint /detect
@app.get(path="/detect")
def detect(body: Body) -> Dict[str, List[List[int]]]:
    detect_face = DetectFace()

    # Processando
    img = body.img
    img = base64_to_nparray(img)
    img = detect_face.bgr_to_gray(img)

    # Deteccao
    res = detect_face.detect(img)

    return {"faces": res}
