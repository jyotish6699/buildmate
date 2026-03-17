import redis
from core.config import settings

class RedisStore:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True
        )

        # ------- SIGNAL QUEUE -------
    def push_signal(self, signal_type: str, user_id: str):
        key = f"signal:{signal_type}"
        self.client.rpush(key, user_id)

    def pop_two_users(self, signal_type: str):
        key = f"signal:{signal_type}"

        if self.client.llen(key) >= 2:
            user1 = self.client.lpop(key)
            user2 = self.client.lpop(key)
            return user1, user2
        return None
    
    def get_queue_length(self, signal_type: str):
        key = f"signal:{signal_type}"
        return self.client.llen(key)
    
    #  ------------ ONLINE USERS -------------
    def add_online_user(self, user_id: str):
        self.client.sadd("online_users", user_id)

    def remove_online_user(self, user_id: str):
        self.client.srem("online_users", user_id)

    def get_online_users(self):
        return self.client.smembers("online_users")
    
    
redis_store = RedisStore()