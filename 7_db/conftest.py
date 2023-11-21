import psycopg2
import pytest
from psycopg2.extras import DictCursor


@pytest.fixture(autouse=True)
def db_connection():
    connection = psycopg2.connect(
        host="psql-mock-database-cloud.postgres.database.azure.com",
        port=5432,
        user="qrjeoikibllaocuiftlkxokl@psql-mock-database-cloud",
        password="bqespdpoqastfoagjpwzogma",
        database="booking1698648427710xchgffvgswkedxka"
    )
    print("Соединение с базой данных установлено")
    return connection

@pytest.fixture(autouse=True)
def cursor(db_connection):
    cursor = db_connection.cursor(cursor_factory=DictCursor)
    return cursor


