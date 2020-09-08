import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        nodes: [],
        edges: []
    },
    mutations: {
        setNodes(state, nodes) {
            state.nodes = nodes
        },
        setEdges(state, edges) {
            state.edges = edges
        }
    },
    actions: {
        setNodes({ commit }, nodes) {
            commit('setNodes', nodes)
        },
        setEdges({ commit }, edges) {
            commit('setEdges', edges)
        }
    },
    modules: {
    }
})
