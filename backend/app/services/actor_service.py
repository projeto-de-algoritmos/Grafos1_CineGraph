from imdb import IMDb


class ActorService():

    def __init__(self):
        self.imdb = IMDb()

    def get_actor_data(self, actor_name: str) -> str:
        actor = self.imdb.search_person(actor_name)[0]

        full_person = self.imdb.get_person(actor.getID())

        return full_person["filmography"]


