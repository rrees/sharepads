from .connection import connect
from .sql import sharepads as sharepads_sql


def create(slug, name=None):
    params = {"slug": slug}

    if name:
        params["name"] = name

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sharepads_sql.insert, params)

            return cursor.fetchone().get("row")


def all():
    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sharepads_sql.all)

            return cursor.fetchall()


def get_by_slug(slug: str):
    params = {
        "slug": slug,
    }

    with connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(sharepads_sql.get_by_slug, params)

            return cursor.fetchone()
