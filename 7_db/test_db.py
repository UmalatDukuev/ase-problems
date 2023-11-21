import allure
import psycopg2
from psycopg2.extras import DictCursor


def create_connection():
    connection = psycopg2.connect(
        host="psql-mock-database-cloud.postgres.database.azure.com",
        port=5432,
        user="qrjeoikibllaocuiftlkxokl@psql-mock-database-cloud",
        password="bqespdpoqastfoagjpwzogma",
        database="booking1698648427710xchgffvgswkedxka"
    )
    return connection

def close_connection(cursor, connection):
    cursor.close()
    connection.close()

@allure.title("Create user test")
def test_create_user():
    connection = create_connection()

    user_id = 3
    user_first_name = "Umalat3"
    user_last_name = "Dukuev3"
    user_email = "dukuev037@mail.ru3"
    cursor = connection.cursor(cursor_factory=DictCursor)
    cursor.execute("INSERT INTO users (id, first_name, last_name, email) VALUES (%s, %s, %s, %s)",
                   (user_id, user_first_name, user_last_name, user_email))
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.commit()
    print(users)
    user = users[len(users) - 1]
    assert user["id"] == user_id
    assert user["first_name"] == user_first_name
    assert user["last_name"] == user_last_name

    close_connection(cursor, connection)


@allure.title("Get user information test")
def test_get_user_info():
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE email = 'dukuev037@mail.ru' ")
    user_info = cursor.fetchall()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    allure.attach(str(user_info), "User Information")
    print(users)
    print(user_info)

    close_connection(cursor, connection)


@allure.title("Update user information test")
def test_update_user_info():
    connection = create_connection()

    # Обновление информации о пользователе
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET first_name = 'Updated Umalat' WHERE email = 'dukuev037@mail.ru3'")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.commit()
    print(users)

    close_connection(cursor, connection)


@allure.title("Delete user test")
def test_delete_user():
    connection = create_connection()

    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE email = 'dukuev037@mail.ru3'")
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    connection.commit()

    print(users)

    close_connection(cursor, connection)