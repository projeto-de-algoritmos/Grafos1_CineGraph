from imdb import IMDb


class ActorService():

    def __init__(self):
        self.imdb = IMDb()

    def get_actor_data(self, actor_name: str) -> str:
        actor = self.imdb.search_person(actor_name)[0]
        # <class 'imdb.Person.Person'>

        #full_person = self.imdb.get_person(actor.getID())
        result = self.imdb.get_person(actor.getID())
        ##############################

        filmography = self.imdb.get_person_filmography(actor.getID())
        #<class 'dict'>

        filmography = filmography["data"]["filmography"]
        #<class 'list'>
        filmography = filmography["data"]["filmography"][0]
        #<class 'dict'>
        chave = "actress"
        if filmography.get("actor", False): # verifica se e um ator ou uma atriz e
            chave = "actor"                 # muda a chave se for ator
        
        filmography = filmography[chave]
        #<class 'list'> de Movie
        filmes = [] # lista de filmes do ator/atriz
        for i in filmography:
            filmes.append(i["title"])
        
        #print("\n" + filmes + "\n")

        #return full_person["filmography"][0]["actress"] #or full_person["filmography"][0]["actor"]

        return result["filmography"]


