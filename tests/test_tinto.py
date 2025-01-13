from fastapi import testclient
import tinto

def user_register_201_return():
    testclient(tinto)