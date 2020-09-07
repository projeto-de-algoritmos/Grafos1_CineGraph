import BaseService from "./BaseService"

class ActorService extends BaseService {
    constructor() {
        super()
    }

    async getActorListByName(name) {
        return await this.client.get(`/actor/list/${name}`)
    }

    async getActorDataById(id, actorNumber) {
        const actorLimit =  actorNumber ? `?actor_number=${actorNumber}` : ""
        return await this.client.get(`/actor/${id}${actorLimit}`)
    }

    async getActorInfoById(id) {
        return await this.client.get(`/info/actor/${id}`)
    }

    async getMovieInfoById(id) {
        return await this.client.get(`/info/movie/${id}`)
    }
}

export default ActorService