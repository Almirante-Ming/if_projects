from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from tinto.schemas import Message, User_Schema, User_public

tinto = FastAPI()

@tinto.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message':'it`s works'}

@tinto.post('/users/', status_code=HTTPStatus.CREATED, response_model=User_public)
def create_user(user: User_Schema):
    return user