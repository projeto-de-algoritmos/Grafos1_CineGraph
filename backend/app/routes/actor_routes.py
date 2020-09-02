from ..controllers.actor_controller import ActorController


class Routes():
    def __init__(self):
        self.actor_controller = ActorController()

    def configure_routes(self, app):

        @app.get("/")
        def read_root():
            return { "Hello": "World" }


        @app.get("/actor/{name}")
        def get_actor_data(name: str):
            return self.actor_controller.get_actor_data(name)