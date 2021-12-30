"""
    @File :   main.py
    @Author : mukul
    @Date :   29-12-2021
"""
from fastapi import FastAPI
from db_connect import DBConnection
from pydantic import BaseModel
from queries import *
app = FastAPI()

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True)


class Reviewer(BaseModel):
    id: int
    first_name: str
    last_name: str


@app.get("/")
def hello_world():
    return {'message':'Welcome To FastAPI CRUD Operations'}


@app.get("/item/{item_id}")
def get_movie(item_id: int):
    """
    desc: created api to get only one item from the table
    :return movie:
    """
    movie = get_one_movie(item_id)
    return movie


@app.get("/item/")
def get_all_movies():
    """
    desc: created api to get all items from the table
    :return list of movies:
    """
    movies = get_movies()
    return movies


@app.post("/add_reviewer/")
def add_reviewer(review_list: Reviewer):
    """
    desc: created api to insert item in the database table
    """
    message = add_user(review_list.id, review_list.first_name, review_list.last_name)
    return message


@app.delete("/delete_reviewer/{id}")
def delete_reviewer(id: int):
    """
    desc: created api to delete the items from the database table using id
    """
    message = delete_user(id)
    return message


@app.put("/update_reviewer/{id}")
def update_reviewer(id: int, rev_list: Reviewer):
    """
    desc: created api to update any item in the database table
    """
    message = update_user(id, rev_list.first_name)
    return message
