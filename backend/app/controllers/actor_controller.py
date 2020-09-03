from ..services.actor_service import ActorService
from fastapi import HTTPException
from typing import List

class ActorController():
    def __init__(self):
        self.actor_service = ActorService()
    
    def get_actor_list(self, name: str) -> List:
        try:
            return self.actor_service.get_actors_by_name(name)
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)

    def get_actor_data(self, actor: str) -> List:
        try:
            actor_data = self.actor_service.get_actor_data(actor)

            return actor_data
        except Exception:
            raise HTTPException(status_code=404, detail=Exception)