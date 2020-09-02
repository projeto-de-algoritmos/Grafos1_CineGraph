from ..services.actor_service import ActorService
from fastapi import HTTPException

class ActorController():
    def __init__(self):
        self.actor_service = ActorService()

    def get_actor_data(self, actor: str) -> str:
        try:
            actor_data = self.actor_service.get_actor_data(actor)

            return actor_data
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)