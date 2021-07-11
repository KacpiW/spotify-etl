import mysql.connector
from mysql.connector import Error, connect


def create_connection(host=None, database=None, user=None, password=None):

    try:
        connection = mysql.connector.connect(
            host=host, database=database, user=user, password=password)

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record[0])

        return connection

    except Error as e:
        print("Error while connecting to MySQL", e)
