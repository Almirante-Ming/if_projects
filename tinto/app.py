from fastapi import FastAPI, HTTPException

tinto = FastAPI()

@tinto.get('/')
def read_rood():
    return {'message':'it`s works'}