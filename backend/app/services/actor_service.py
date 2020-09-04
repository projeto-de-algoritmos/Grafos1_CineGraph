from imdb import IMDb
from typing import List


class ActorService():

    def __init__(self):
        self.imdb = IMDb()
        self.current_actor = ""

    def get_actors_by_name(self, actor_name: str) -> List:
        actorList = []
        imdbActorList = self.imdb.search_person(actor_name, )
        
        for people in imdbActorList[0:6]:
            headshot = people.get("headshot")
            if not headshot:
                headshot = "https://img.icons8.com/cotton/2x/person-male.png"
            actorList.append({
                "name": people['name'],
                "headshot": headshot,
                "id": people.getID()
            })

        return actorList

    def get_actor_data(self, id: str) -> List:

        full_person = self.imdb.get_person(id, info=['main'])
        movieListByActor = self.__get_movieset_from_person(full_person)
        self.current_actor = full_person.get('name')
        return [{
            "person": self.current_actor,
            "person_image": full_person.get('headshot'),
            "movies": movieListByActor,
            "person_id": full_person.getID()
        }]

    def __get_movieset_from_person(self, person) -> List:
        movieListByActor = []
        
        try:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actor")), None)['actor']
        except Exception:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actress")), None)['actress']

        for movie in full_person_movieset[0:15]:
            localMovie = self.get_movie_data(movie.getID())
            movieListByActor.append({
                "title":  localMovie.get('title'),
                "id": localMovie.movieID,
                "cover": localMovie.get('cover'),
                "cast": self.get_movie_cast(localMovie.get('cast')[0:5])
            })

        return movieListByActor
    
    def get_movie_data(self, movieID: str) -> List:
        return self.imdb.get_movie(movieID)

    def get_movie_cast(self, movie) -> List:
        
        def _mount_data_cast(person):
            return {
                "person": person.get('name'),
                "person_id": person.getID()
            }

        return [ _mount_data_cast(person) for person in movie if person.get('name') is not self.current_actor ]