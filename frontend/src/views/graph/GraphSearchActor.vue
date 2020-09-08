<template>
    <div>
        <div class="d-flex align-center">
            <v-text-field
                v-model="actorName"
                hide-details
                label="(BFS) Pesquisar ator/atriz em comum"
                placeholder="Insira o termo de busca"
                clearable />

                <v-btn
                    color="primary"
                    text
                    @click="searchPerson">
                    <v-icon>mdi-magnify</v-icon>
                </v-btn>
        </div>

        <div
            class="pt-3" 
            v-if="matchedActors.length"> 
            <ul>
                <li v-for="actor in matchedActors"
                    :key="actor.id">
                    {{ actor.label }}
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import { mapState } from "vuex"

export default {
    data: () => ({
        adjacentList: {},
        matchedActors: [],
        actorName: ""
    }),
    computed: {
        ...mapState(['nodes', 'edges'])
    },
    methods: {
        searchPerson() {
            this.matchedActors = []

            // Monta a lista de adjacências
            this.mountAdjacentList(this.actorName)

            if (this.actorName && !this.matchedActors.length) {

                // Crio uma cópia local dos nós
                const unexploredLocalNodes = JSON.parse(JSON.stringify(this.nodes))
                const enqueue = []



                for(let unexploredNode of unexploredLocalNodes){
                    if (!unexploredNode.visited) {
                        // Adiciono o nó na fila
                        enqueue.push(unexploredNode)
        
                        // Marco o nó como visitado
                        unexploredNode.visited = true
        
                        
                        // Verifico se o ator tem o nome parecido com o que foi informado
                        if (unexploredNode.label.toLowerCase().includes(this.actorName.toLowerCase())) {
                            this.matchedActors.push(unexploredNode)
                        }

                        console.log(unexploredNode.label)
        
                        while(enqueue.length > 0) {
        
                            // Removo o primeiro elemento da fila e salvo ele
                            let nextNode = enqueue.shift()

                            // Verifico se o nó possui vizinhos com base na lista de adjacências
                            if (this.adjacentList[nextNode.id]) {
                                // Itero sobre os vizinhos (ngb) com base na lista de adjacencias
                                for (let ngb of this.adjacentList[nextNode.id]) {
                                    let ngbNode = unexploredLocalNodes.find(node => node.id == ngb.to)
            
                                    // Verifico se o nó já foi visitado
                                    if (!ngbNode.visited) {
                                        ngbNode.visited = true
                                        enqueue.push(ngbNode)
                                    }     
                                }
                            }
                        }
                    }
                }

                if (!this.matchedActors.length) {
                    this.matchedActors.push({ 
                        id: -1,
                        label: "Nenhum ator/atriz encontrado"
                    })
                }
            }

        },
        mountAdjacentList() {
            this.edges.map(edge => {
                if(this.adjacentList[edge.from]) {
                    this.adjacentList[edge.from].push(edge)
                }
                else {
                    this.adjacentList[edge.from] = [ edge ]
                }
            }, this)
        }
    },
    watch: {
        actorName: function(val) {
            if (!val) {
                this.matchedActors = []
            }
        }
    }
}
</script>