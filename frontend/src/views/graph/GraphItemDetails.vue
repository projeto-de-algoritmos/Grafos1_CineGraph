<template>
    <section id="graph-item-detais">
        <div v-if="type && type === 'person'">
            <v-card>
                <img :src="actor.image" alt="" class="img">
                <h2>{{ actor.name }}</h2>
            </v-card>
        </div>
        <div v-else-if="type && type === 'movie'">
            <v-card>
                <img :src="movie.cover" alt="" class="img">
                <h2>{{ movie.title }} - {{ movie.year }}</h2>
                <h4>{{ movie.plot }}</h4>
            </v-card>
        </div>
        <v-overlay 
            absolute
            :value="loading">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>
    </section>
</template>

<script>
import ActorService from '../../services/ActorService'

const actorService = new ActorService()
export default {
    props: {
        itemId: {
            type: String,
            required: false,
            default: ""
        },
        type: {
            type: String,
            required: false,
            default: ""
        }
    },
    data: () => ({
        actor: {
            image: "",
            name: ""
        },
        movie: {
            cover: "",
            title: "",
            plot: "",
            year: ""
        },
        loading: false
    }),
    methods: {
        async getActorInfo(id) {
            try {
                const response = await actorService.getActorInfoById(id)

                this.actor = response.data
            } catch (e) {
                console.error(e)
            }
        },
        async getMovieInfo(id) {
            try {
                const response = await actorService.getMovieInfoById(id)

                this.movie = response.data
            } catch (e) {
                console.error(e)
            }
        }
    },
    watch: {
        itemId: async function(val) {
            debugger
            if (val) {
                if (this.type && this.type === 'movie') {
                    this.loading = true
                    this.actor = {
                        image: "",
                        name: ""
                    }
                    await this.getMovieInfo(val)
                }
                else {
                    this.loading = true
                    this.movie = {
                        cover: "",
                        title: "",
                        plot: "",
                        year: ""
                    },
                    await this.getActorInfo(val)
                }
                this.loading = false
            }
        }
    }

}
</script>

<style lang="scss">
#graph-item-detais {
    position: relative;

    .img {
        width: 100%;
        object-fit: contain;
    }
}
</style>