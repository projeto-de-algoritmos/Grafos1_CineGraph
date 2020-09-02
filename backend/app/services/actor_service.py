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

        quantity = 5 # max 5 movies and max 5 people cast
        countMovies = 0 # movie counter
        countPeople = 0 # people counter

        movies = [{}]

        for i in filmes:
            if countMovies==quantity:
                break
            filme = self.imdb.search_movie(i)
            filme = filme[0]
            movies[0]["movie_%d" % countMovies] = [{"data":""},{"cast":""}]
            movies[0]["movie_%d" % countMovies][0]["data"] = filme.data
            movies[0]["movie_%d" % countMovies][1]["cast"] = []
            # above: movie data, such as title, kind, year, cover url
            filme = self.imdb.get_movie(filme.movieID)
            for j in filme.data["cast"]:
                if countPeople==quantity:
                    break
                personID = j.personID
                personData = self.imdb.get_person_main(personID)
                movies[0]["movie_%d" % countMovies][1]["cast"].append(personData) # corrigir aqui
                countPeople+=1
            countPeople = 0
            countMovies+=1

        #return full_person["filmography"][0]["actress"] #or full_person["filmography"][0]["actor"]

        return result["filmography"]


