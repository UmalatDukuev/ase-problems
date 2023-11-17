import allure
from psycopg2.extras import DictCursor
import pytest
import psycopg2


class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(
            host="psql-mock-database-cloud.postgres.database.azure.com",
            port=5432,
            user="qrjeoikibllaocuiftlkxokl@psql-mock-database-cloud",
            password="bqespdpoqastfoagjpwzogma",
            database="booking1698648427710xchgffvgswkedxka"
        )
        print("Соединение с базой данных установлено")
        self.cursor = self.connection.cursor(cursor_factory=DictCursor)

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Соединение с базой данных закрыто")


def close_connection(cursor, connection):
    cursor.close()
    connection.close()


data = {
    "user_id": 1,
    "user_first_name": "Umalat",
    "user_last_name": "Dukuev",
    "user_email": "dukuev037@mail.ru",
}


@allure.title("Create user test")
def test_create_user(db_connection):
    connection, cursor = db_connection

    cursor.execute("INSERT INTO users (id, first_name, last_name, email) VALUES (%s, %s, %s, %s)",
                   (data["user_id"], data["user_first_name"], data["user_last_name"], data["user_email"]))
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print(users)
    user = users[len(users) - 1]
    assert user["id"] == data["user_id"]
    assert user["first_name"] == data["user_first_name"]
    assert user["last_name"] == data["user_last_name"]
    assert user["email"] == data["user_email"]


@allure.title("Get user information test")
def test_get_user_info(db_connection):
    connection, cursor = db_connection
    cursor.execute("SELECT * FROM users WHERE email = 'dukuev037@mail.ru'")
    user_info = cursor.fetchall()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    allure.attach(str(user_info), "User Information")
    print(users)
    print(user_info)
    for user in user_info:
        assert user["email"] == data["user_email"]

@allure.title("Update user information test")
def test_update_user_info(db_connection):
    connection, cursor = db_connection
    cursor.execute("UPDATE users SET first_name = 'Updated Umalat' WHERE email = 'dukuev037@mail.ru'")
    cursor.execute("SELECT * FROM users where email = 'dukuev037@mail.ru'")
    users = cursor.fetchall()
    connection.commit()
    print(users)
    for user in users:
        assert user["first_name"] == 'Updated Umalat'


@allure.title("Delete user test")
def test_delete_user(db_connection):
    connection, cursor = db_connection
    cursor.execute("DELETE FROM users WHERE email = 'dukuev037@mail.ru20'")
    cursor.execute("SELECT * FROM users WHERE email = 'dukuev037@mail.ru20'")
    users = cursor.fetchall()
    connection.commit()
    print(users)
    assert users == []
