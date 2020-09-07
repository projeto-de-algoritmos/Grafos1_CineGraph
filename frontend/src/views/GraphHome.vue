
<template>
    <section id="home-graph">
        <div class="d-flex graph-container pa-4">
            <GraphSearch
                :type="type"
                :item-id="itemId"
                @selectedActor="changeCurrentActor"/>
            
            <GraphRender 
                @selectedNode="changeValues"
                :actor-limit="actorLimit"
                :actor="selectedActor"/>
        </div>
    </section>
</template>

<script>
import GraphSearch from "./graph/GraphSearch"
import GraphRender from "./graph/GraphRender"

export default {
    data: () => ({
        selectedActor: "",
        type: "",
        itemId: "",
        actorLimit: null
    }), 
    components: {
        GraphSearch,
        GraphRender
    },
    methods: {
        changeCurrentActor(value) {
            this.selectedActor = value.actor
            this.actorLimit = value.actorLimit
        },
        changeValues({ type, id }) {
            debugger
            this.type = type
            this.itemId = id
        }
    }
}
</script>

<style lang="scss">
#home-graph {
    height: 100%;
    display: flex;

    .graph-container {
        overflow: hidden;
        flex-grow: 1;
    }
}
</style>