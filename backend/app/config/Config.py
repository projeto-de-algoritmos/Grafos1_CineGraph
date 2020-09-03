import os

class Config():
    def __init__(self):
        self.config = {
            "api": {
                "port": os.getenv("PORT")
            }
        }