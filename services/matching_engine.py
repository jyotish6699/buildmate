from storage.redis_store import redis_store

from realtime.websocket_manager import websocket_manager


class MatchingEngine:

    async def try_match(self, signal_type: str):
        result = redis_store.pop_two_users(signal_type)

        if result:
            user1, user2 = result

            match_data = {
                "type": "match_found",
                "signal_type": signal_type,
                "partner_id": user2
            }

            # send to user1
            await websocket_manager.send_to_user(user1, match_data)

            # send to user2(reverse partner)
            match_data["partner_id"] = user1
            await websocket_manager.send_to_user(user2, match_data)

            return {
                "user_a": user1,
                "user_b": user2,
                "signal_type": signal_type
            }
        return None
    
matching_engine = MatchingEngine()
