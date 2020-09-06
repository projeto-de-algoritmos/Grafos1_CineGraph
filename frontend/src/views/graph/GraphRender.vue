<template>
    <section id="renderer">
        <v-overlay :value="loading">
            <v-progress-circular indeterminate size="64"></v-progress-circular>
        </v-overlay>

        <Network ref="network"
            :nodes="nodes"
            :edges="edges"
            :options="options">
        </Network>

        <div id="graph" style="heigth: 100%"></div>
    </section>
</template>

<script>
import ActorService from '../../services/ActorService'
import { Network } from "vue-vis-network";
import "vue-vis-network/node_modules/vis-network/dist/vis-network.css";


const actorService = new ActorService()

export default {
    components: {
        Network
    },
    data: () => ({
        "nodes": [],
        "edges": [],
        options: {
            nodes: {
                borderWidth: 4
            },
            edges: {
                color: 'green'
            }
        },
        loading: false,
        network: undefined,
    }),
    props: {
        actor: {
            type: String,
            required: false,
            default: ""
        }
    },
    methods: {
        async getActorData(id) {
            const response = await actorService.getActorDataById(id)

            this.nodes = response.data.nodes
            this.edges = response.data.edges
        },
    },
    watch: {
        actor: async function(val) {
            if (val) {
                this.loading = true
                await this.getActorData(val)
                this.loading = false
            }
        }
    }

}
</script>

<style lang="scss">

#renderer {
    height: 750px;

    .vis-network {
        height: 750px;
    }
}

</style>