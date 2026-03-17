from storage.redis_store import redis_store
from storage.postgres_store import postgres_store

from realtime.websocket_manager import websocket_manager


from storage.postgres_store import postgres_store

class MatchingEngine:

    async def try_match(self, signal_type: str):
        result = redis_store.pop_two_users(signal_type)

        if result:
            user1, user2 = result

            # 1. Save match
            match_id = postgres_store.create_match(signal_type, user1, user2)

            # 2. Create session
            session_id = postgres_store.create_session(match_id)

            # 3. Notify users
            await websocket_manager.send_to_user(user1, {
                "type": "match_found",
                "signal_type": signal_type,
                "partner_id": user2,
                "match_id": match_id,
                "session_id": session_id
            })

            await websocket_manager.send_to_user(user2, {
                "type": "match_found",
                "signal_type": signal_type,
                "partner_id": user1,
                "match_id": match_id,
                "session_id": session_id
            })

            return {
                "match_id": match_id,
                "session_id": session_id,
                "user_a": user1,
                "user_b": user2,
                "signal_type": signal_type
            }

        return None
    
matching_engine = MatchingEngine()
