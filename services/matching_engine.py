from storage.redis_store import redis_store

class MatchingEngine:

    def try_match(self, signal_type: str):
        result = redis_store.pop_two_users(signal_type)

        if result:
            user1, user2 = result

            return {
                "user_a": user1,
                "user_b": user2,
                "signal_type": signal_type
            }
        return None
    
matching_engine = MatchingEngine()
