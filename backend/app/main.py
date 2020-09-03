from fastapi import FastAPI
import uvicorn
from .routes.actor_routes import Routes
from .config.Config import Config
from .config.debug import debug_configurations

config = Config().config
app = FastAPI()

Routes().configure_routes(app)

debug_configurations()