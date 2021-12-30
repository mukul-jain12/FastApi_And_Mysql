"""
    @File :   main.py
    @Author : mukul
    @Date :   29-12-2021
"""
from fastapi import FastAPI
from db_connect import DBConnection
from pydantic import BaseModel
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
    show_data_query = f"SELECT * FROM movies WHERE id={item_id}"
    cursor.execute(show_data_query)
    list1 = []
    for i in cursor:
        list1.append(i)
    return list1


@app.get("/item/")
def get_all_movies():
    """
    desc: created api to get all items from the table
    :return list of movies:
    """
    show_data_query = "select * from movies"
    cursor.execute(show_data_query)
    list1 = []
    for i in cursor:
        list1.append(i)
    return list1


@app.post("/add_reviewer/")
def add_reviewer(review_list: Reviewer):
    """
    desc: created api to insert item in the database table
    """
    show_data_query = "INSERT INTO reviewers (id, first_name, last_name) VALUES (%d, '%s', '%s')"%(review_list.id, review_list.first_name, review_list.last_name)
    cursor.execute(show_data_query)
    connection.commit()
    return "Data saved!!"


@app.delete("/delete_reviewer/{id}")
def update_reviewer(id: int):
    """
    desc: created api to delete the items from the database table using id
    """
    show_data_query = "delete from reviewers where id = %d"%(id)
    cursor.execute(show_data_query)
    connection.commit()
    return "Data deleted!!"


@app.put("/update_reviewer/{id}")
def update_reviewer(id: int, rev_list: Reviewer):
    """
    desc: created api to update any item in the database table
    """
    show_data_query = "update reviewers set first_name = '%s' where id = %d"%(rev_list.first_name, id)
    cursor.execute(show_data_query)
    connection.commit()
    return "Data updated!!"
