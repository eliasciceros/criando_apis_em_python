"""
    API para CRUD de estudantes utilizando:
        - fastapi como framework de criacao de API
        - sqlmodel como ORM

    Modo de utilizacao:
        - Inicie o ambiente e acesse o endereco "localhost:PortaEscolhida"

    P.S.: para iniciar o ambiente, execute no terminal deste diretorio:
        - uvicorn app:app --port 8081 --reload
        - Se uvicorn não é reconhecido como comando interno, execute:
            - python -m uvicorn app:app --port 8081 --reload
"""
__author__ = "Elias Cícero Moreira Guedes"
__date__ = "26 de Setembro de 2021"
__credits__ = ["Igor Souza, ministrante do curso 'Criando APIs em Python'"]

from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlalchemy
from sqlmodel import create_engine, SQLModel, Field, Session, select
import os

app = FastAPI()


class StudentModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    phone: str
    school: str


engine = create_engine("sqlite:///crud.db")

if not os.path.isfile("crud.db"):
    SQLModel.metadata.create_all(engine)


class StudentBody(BaseModel):
    id: Optional[int]
    name: str
    age: Optional[int] = None
    phone: Optional[str] = None
    school: Optional[str] = None


def get_StudentModel_from_StudentBody(body: StudentBody):
    return StudentModel(
        id=body.id,
        name=body.name,
        age=body.age,
        phone=body.phone,
        school=body.school
    )


@app.get("/student")
def retrieve_student():
    with Session(engine) as session:
        query = select(StudentModel)
        students = session.exec(query)
        students_list = [std for std in students]

    return {"students": students_list}


@app.post("/student", status_code=201)
def create_student(student: StudentBody):
    with Session(engine) as session:
        session.add(get_StudentModel_from_StudentBody(body=student))

        session.commit()
    return "OK"


@app.get("/student/{id}")
def retrieve_single_student(id: int):
    try:
        with Session(engine) as session:
            statement = select(StudentModel).where(StudentModel.id == id)
            student = session.exec(statement).one()
            return {"student": student}
    except sqlalchemy.exc.NoResultFound:
        raise HTTPException(status_code=400, detail="Student not found.")



@app.put("/student/{id}")
def update_single_student(id: int, new_attributes: StudentBody):
    try:
        with Session(engine) as session:
            statement = select(StudentModel).where(StudentModel.id == id)
            student = session.exec(statement).one()

            if new_attributes.name:
                student.name = new_attributes.name
            if new_attributes.age:
                student.age = new_attributes.age
            if new_attributes.phone:
                student.phone = new_attributes.phone
            if new_attributes.school:
                student.school = new_attributes.school

            session.add(student)
            session.commit()
            session.refresh(student)

        return {"student": student}

    except sqlalchemy.exc.NoResultFound:
        raise HTTPException(status_code=400, detail="Student not found.")


@app.delete("/student/{id}")
def delete_single_student(id: int):
    try:
        with Session(engine) as session:
            statement = select(StudentModel).where(StudentModel.id == id)
            student = session.exec(statement).one()
            session.delete(student)
            session.commit()
            return {"msg": f"Student with id={id} has been deleted!"}
    except sqlalchemy.exc.NoResultFound:
        raise HTTPException(status_code=400, detail="Student not found.")
