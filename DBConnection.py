import mysql.connector

def queryDB(string):
    connection = mysql.connector.connect(user='root', host='localhost', password='123456')
    cursor = connection.cursor()
    cursor.execute(string)
    return cursor.fetchall()
