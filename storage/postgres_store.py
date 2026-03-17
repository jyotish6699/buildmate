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
            
    def create_match(self, signal_type, user_a, user_b):
        query = """
        INSERT INTO matches (signal_type, user_a, user_b)
        VALUES (%s, %s, %s)
        RETURNING match_id;
        """
        result = self.execute(query, (signal_type, user_a, user_b), fetch=True)
        return result[0]["match_id"]

    def create_session(self, match_id):
        query = """
        INSERT INTO sessions (match_id)
        VALUES (%s)
        RETURNING session_id;
        """
        result = self.execute(query, (match_id,), fetch=True)
        return result[0]["session_id"]
            
postgres_store = PostgresStore()