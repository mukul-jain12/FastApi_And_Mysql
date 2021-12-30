"""
    @File :   main.py
    @Author : mukul
    @Date :   29-12-2021
"""
import datetime

from fastapi import FastAPI
from db_connect import DBConnection
from pydantic import BaseModel
app = FastAPI()

connection = DBConnection.establish_connection()
cursor = connection.cursor()


class Movie(BaseModel):
    id: int
    title: str
    release_year: str
    genre: str
    collection_in_mil: float


@app.get("/item/{item_id}")
def get_movie(item_id: int):
    show_data_query = f"SELECT * FROM movies WHERE id={item_id}"
    cursor.execute(show_data_query)
    list1 = []
    for i in cursor:
        list1.append(i)
    return list1


@app.get("/item/")
def get_all_movies():
    show_data_query = "select * from movies"
    cursor.execute(show_data_query)
    list1 = []
    for i in cursor:
        list1.append(i)
    return list1
