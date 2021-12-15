import mysql.connector, json

HOST = '@IP_DATABASE'
USER = 'USER'
PASS = 'PASSWORD'


class Database:

    def __init__(self,database) -> None:
        self.database = database

    def connection(self) -> mysql.connector:
        mydb = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASS,
            database=self.database
        )
        return mydb

    def insert(self, sql):
        db = self.connection()
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()

    def select(self, sql):
        db = self.connection()
        cursor = db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
