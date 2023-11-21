import psycopg2
import pytest


@pytest.fixture(autouse=True)
def db_connection():
    connection = psycopg2.connect(
        host="psql-mock-database-cloud.postgres.database.azure.com",
        port=5432,
        user="qrjeoikibllaocuiftlkxokl@psql-mock-database-cloud",
        password="bqespdpoqastfoagjpwzogma",
        database="booking1698648427710xchgffvgswkedxka"
    )
    return connection