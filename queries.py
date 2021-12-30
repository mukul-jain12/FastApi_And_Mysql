"""
    @File :   queries.py
    @Author : mukul
    @Date :   30-12-2021
"""
from db_connect import DBConnection

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True)


def get_one_movie(movie_id):
    """
    desc: query to get a movie from database
    """
    show_data_query = f"SELECT * FROM movies WHERE id={movie_id}"
    cursor.execute(show_data_query)
    movie = [i for i in cursor]
    return movie


def get_movies():
    """
    desc: query to get all movies from database
    """
    show_data_query = "select * from movies"
    cursor.execute(show_data_query)
    movies = [i for i in cursor]
    return movies


def add_user(user_id, first_name, last_name):
    """
    desc: query to insert user in the database table
    """
    show_data_query = "insert into reviewers (id, first_name, last_name) values(%d, '%s', '%s')" % (
        user_id, first_name, last_name)
    cursor.execute(show_data_query)
    connection.commit()
    return "Reviewer Details Saved in Database!!"


def delete_user(user_id):
    """
    desc: query to delete user from database table
    """
    show_data_query = "delete from reviewers where id = %d" % user_id
    cursor.execute(show_data_query)
    connection.commit()
    return "Reviewer Details Deleted From Database!!"


def update_user(user_id, first_name):
    """
    desc: query to update user detail in the database table
    """
    show_data_query = "update reviewers set first_name = '%s' where id = %d" % (first_name, user_id)
    cursor.execute(show_data_query)
    connection.commit()
    return "Reviewer Details Updated!!"
