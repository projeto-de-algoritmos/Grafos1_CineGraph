from ..controllers.actor_controller import ActorController


class Routes():
    def __init__(self):
        self.actor_controller = ActorController()

    def configure_routes(self, app):

        @app.get("/actor/list/{name}")
        def get_actor_data(name: str):
            return self.actor_controller.get_actor_list(name)

        @app.get("/actor/{id}")
        async def get_actor_data(id: str):
            return await self.actor_controller.get_actor_data(id)