from imdb import IMDb
from typing import List
import asyncio
from asyncio import as_completed, gather

class ActorService():

    def __init__(self):
        self.imdb = IMDb()
        self.current_actor = ""
        self.movie_fallback_image = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcR6pdTz5L8m-BnQaPfYvrKXSpvTxri_DDtSqw&usqp=CAU"
        self.actor_fallback_image = "https://img.icons8.com/cotton/2x/person-male.png"

    def get_actors_by_name(self, actor_name: str) -> List:
        actorList = []
        imdbActorList = self.imdb.search_person(actor_name, )
        
        for people in imdbActorList[0:10]:
            headshot = people.get("headshot") or self.actor_fallback_image
            actorList.append({
                "name": people['name'],
                "headshot": headshot,
                "id": people.getID()
            })

        return actorList

    async def get_actor_data(self, id: str) -> List:

        full_person = self.imdb.get_person(id, info=['main'])
        movieListByActor = await self.__get_movieset_from_person(full_person)
        self.current_actor = full_person.get('name')

        initial_structure = {
            "person": self.current_actor,
            "person_image": full_person.get('headshot'),
            "movies": movieListByActor,
            "person_id": full_person.getID()
        }

        nodes = self.mount_graph_structure(initial_structure)
        edges = self.mount_edges_structure(initial_structure)

        return {
            "nodes": nodes, 
            "edges": edges
        }

    async def __get_movieset_from_person(self, person) -> List:
        movieListByActor = []
        
        try:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actor")), None)['actor']
        except Exception:
            full_person_movieset = next((item for item in person['filmography'] if item.get("actress")), None)['actress']

        tasks = []
        for movie in full_person_movieset[0:12]:
            task = asyncio.ensure_future(self.get_movie_data(movie.getID()))
            tasks.append(task)

        results = await gather(*tasks, return_exceptions=True)


        for movie in  results:
            movieListByActor.append({
                "title":  movie.get('title'),
                "id": movie.movieID,
                "cover": movie.get('cover') or self.movie_fallback_image,
                "cast": self.get_movie_cast(movie.get('cast')[0:8])
            })

        return movieListByActor
    
    async def get_movie_data(self, movieId: str) -> List:
        return self.imdb.get_movie(movieId, info=['main'])

    def get_movie_cast(self, movie) -> List:
        
        def _mount_data_cast(person):
            return {
                "person": person.get('name'),
                "person_id": person.getID()
            }

        return [ _mount_data_cast(person) for person in movie if person.get('name') is not self.current_actor ]

    def mount_graph_structure(self, data: dict) -> List:

        nodes = []

        nodes.append({
            "label": data.get('person'),
            "id": data.get('person_id'),
            "identificator": "person"
        })

        for movie in data.get("movies"):
            nodes.append({
                "label":  movie.get('title'),
                "id": movie.get("id"),
                "image": movie.get('cover'),
                "shape": "circularImage",
                "identificator": "movie"
            })

            for person in movie.get("cast"):
                if  self.__person_in_nodes_list(person, nodes):
                    nodes.append({
                        "label": person.get('person'),
                        "id": person.get('person_id'),
                        "identificator": "person"
                    })

        return nodes

    def mount_edges_structure(self, data: dict) -> List:
        edges = []

        for movie in data.get("movies"):
            edges.append({
                "from":  data.get('person_id'),
                "to": movie.get("id")
            })

            for person in movie.get("cast"):
                
                if  self.__edge_in_edge_list(person.get('person_id'), movie.get("id"), edges):
                    edges.append({
                        "from":  person.get('person_id'),
                        "to": movie.get("id")
                    })

        return edges
    def __edge_in_edge_list(self, fromId: str, toId: str, edgeList: List) -> bool:
        return next((edge for edge  in edgeList if edge.get("from") == fromId and edge.get("to") == toId ), None) == None

    def __person_in_nodes_list(self, person: dict, nodelist: List) -> bool:
        return next((tempPerson for tempPerson in nodelist if tempPerson.get("label") == person.get("person")), None) == None