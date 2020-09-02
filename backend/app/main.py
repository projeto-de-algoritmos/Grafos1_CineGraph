from fastapi import FastAPI
from .routes.actor_routes import Routes


app = FastAPI()

Routes().configure_routes(app)
