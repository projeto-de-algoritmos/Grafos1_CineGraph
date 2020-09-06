
<template>
    <section id="home-graph">
        <div class="d-flex graph-container pa-4">
            <GraphSearch
                @selectedActor="changeCurrentActor"/>
            
            <GraphRender 
                :actor="selectedActor"/>
        </div>
    </section>
</template>

<script>
import GraphSearch from "./graph/GraphSearch"
import GraphRender from "./graph/GraphRender"

export default {
    data: () => ({
        selectedActor: ""
    }), 
    components: {
        GraphSearch,
        GraphRender
    },
    methods: {
        changeCurrentActor(value) {
            this.selectedActor = value
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