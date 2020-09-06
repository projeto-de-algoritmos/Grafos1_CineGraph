import BaseService from "./BaseService"

class ActorService extends BaseService {
    constructor() {
        super()
    }

    async getActorListByName(name) {
        return await this.client.get(`/actor/list/${name}`)
    }

    async getActorDataById(id) {
        return await this.client.get(`/actor/${id}`)
    }
}

export default ActorService