import psycopg2
import pytest
from psycopg2.extras import DictCursor
from test_db import DBManager

@pytest.fixture(autouse=True)
def db_connection():
    db_manager = DBManager()
    db_manager.connect()
    yield db_manager.connection, db_manager.cursor

