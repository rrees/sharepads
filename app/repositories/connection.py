import os

import psycopg

from psycopg.rows import dict_row

DB_URL = os.environ["DATABASE_URL"]


def connect():
    return psycopg.connect(DB_URL, row_factory=dict_row)
