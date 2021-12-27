import mysql.connector
from utilities import base

mydb = None


def connect():
    base.mydb = mysql.connector.connect(
        host="remotemysql.com",
        database="Yov2TeLlUN",
        user="Yov2TeLlUN",
        password="OoR9mryQTr")


def reade_from_db():
    connect()
    query = "SELECT * FROM Users"
    my_cursor = base.mydb.cursor()
    my_cursor.execute(query)
    result = my_cursor.fetchall()
    base.data_list = result
    base.mydb.close()

