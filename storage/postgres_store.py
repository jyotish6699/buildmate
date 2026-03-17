import psycopg2
from psycopg2.extras import RealDictCursor
from core.config import settings

class PostgresStore:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=settings.POSTGRES_HOST,
            port=settings.POSTGRES_PORT,
            dbname=settings.POSTGRES_DB,
            user=settings.POSTGRES_USER,
            password=settings.POSTGRES_PASSWORD
        )

    def execute(self, query, params=None, fetch=False):
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, params)
            self.conn.commit()
            if fetch:
                return cursor.fetchall()
            
postgres_store = PostgresStore()