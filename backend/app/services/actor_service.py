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
            movieID = movie.movieID
            cover_url = self.__get_movie_cover_url(movieID)
            #cast = self.__get_movie_cast(movieID)
            movieListByActor.append({
                "title":  movie['title'],
                "id": movieID,
                "cover url": cover_url#,
                #"cast": cast
            })
            countMovies += 1

        return movieListByActor

    def __get_movie_cover_url(self, movieID) -> str:
        movie = self.imdb.get_movie(movieID)
        cover_url = movie.data["cover url"]
        return cover_url

    def __get_movie_cast(self, movieID) -> List:
        movie = self.imdb.get_movie(movieID)
        cast = movie.get("cast")
        if not cast:
            return [] # it is posible that a movie has no cast
        movieCast = []
        maxCast = 6 # maximum 6 people to get
        countCast = 0
        for person in cast:
            if countCast==maxCast:
                break
            id = person.personID
            personData = self.imdb.get_person(id)
            name = personData.get("name")
            birth_place = personData.get("birth notes")
            headshot = personData.get("headshot")
            birth_date = personData.get("birth date")
            movieCast.append({
                "name": name,
                "birth place": birth_place,
                "birth date": birth_date,
                "headshot": headshot
            })
            countCast += 1
        return movieCast
