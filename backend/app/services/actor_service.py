from imdb import IMDb
from typing import List


class ActorService():

    def __init__(self):
        self.imdb = IMDb()

    def get_actors_by_name(self, actor_name: str) -> List:
        actorList = []
        imdbActorList = self.imdb.search_person(actor_name, )
        
        for people in imdbActorList:
            actorList.append({
                "name": people['name'],
                "id": people.getID()
            })

        return actorList

    def get_actor_data(self, id: str) -> List:

        full_person = self.imdb.get_person(id, info=['main'])
        movieListByActor = self.__get_movieset_from_person(full_person)

        return [{
            "person": full_person.get('name'),
            "person_image": full_person.get('headshot'),
            "movies": movieListByActor
        }]

    def __get_movieset_from_person(self, person) -> List:
        movieListByActor = []
        maxMovies = 5 # maximun 5 movies to get
        countMovies = 0
        
        try:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actor")), None)['actor']
        except Exception:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actress")), None)['actress']

        for movie in full_person_movieset:
            if countMovies>=5:
                break
            movieListByActor.append({
                "title":  movie['title'],
                "id": movie.movieID
            })
            countMovies += 1

        return movieListByActor