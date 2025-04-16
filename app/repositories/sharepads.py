from .connection import connect


def create(slug, name=None):
    with connect() as conn:
        with conn.cursor() as cursor:
            pass
