<template>
    <section 
        id="render-graph"
        class="px-3">
        <v-card class="render-graph-card">
            <Network ref="network"
                :nodes="nodes"
                :edges="edges"
                :options="options"
                @select-node="onNodeSelected">
            </Network>
        
            <v-overlay 
                absolute
                :value="loading">
                <div class="d-flex flex-column align-center">
                    <v-progress-circular indeterminate size="64"></v-progress-circular>
                    <h2>Carregando dados da api. Isso pode levar algum tempo...</h2>
                </div>
            </v-overlay>
        </v-card>
    </section>
</template>

<script>
import ActorService from '../../services/ActorService'
import { Network } from "vue-vis-network";
import "vue-vis-network/node_modules/vis-network/dist/vis-network.css";
import { mapActions, mapState } from "vuex"

const actorService = new ActorService()

export default {
    components: {
        Network
    },
    props: {
        actor: {
            type: String,
            required: false,
            default: ""
        },
        actorLimit: {
            type: Number,
            required: false,
            default: 8
        }
    },
    data: () => ({
        options: {
            nodes: {
                borderWidth: 2
            },
            edges: {
                arrows: 'to'
            }
        },
        loading: false,
        network: undefined,
    }),
    computed: {
        ...mapState(['nodes', 'edges'])
    },
    methods: {
        ...mapActions(["setNodes", "setEdges"]),
        async getActorData(id) {
            const response = await actorService.getActorDataById(id, this.actorLimit)

            this.setNodes(response.data.nodes)
            this.setEdges(response.data.edges)
        },
        onNodeSelected(value) {
            const payload = this.$refs.network.nodes.find(item => item.id == value.nodes[0])

            this.$emit("selectedNode", {
                type: payload.identificator,
                id: payload.id
            })
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

#render-graph {
    width: 100%;
    flex-grow: 1;
    position: relative;

    .render-graph-card {
        height: 100%;
        width: 100%;

        > div {
            height: 100%;
            width: 100%;

            canvas {
                max-height: calc(100vh - 110px) !important;
            }
        }
        .vis-network {
            min-height: 650px !important;
        }
    }
}

</style>