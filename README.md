# CineGraph

**Número da Lista**: Não se aplica<br>
**Conteúdo da Disciplina**: Grafos<br>

<hr>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 15/0009011 |  Elias Bernardo |
| 17/0141161  |  Erick Giffoni |

<hr>

## Sobre 
Esse projeto tem como objetivo mostrar os relacionamentos<br>
entre atores/atrizes de cinema e os filmes em que eles<br>
participaram, utilizando o conceito de grafos.

O usuário interage com o software por meio de um navegador<br>
web da preferência dele. Existe uma barra de pesquisa na qual<br>
é possível buscar por um nome de uma atriz ou de um ator.<br>

Ao selecionar um ator ou atriz e fazer a busca, nosso projeto<br>
colhe informações tais como: nome e foto do ator ou da atriz;<br>
filmes que ele ou ela participou; outros atores ou atrizes que<br>
fizeram parte do elenco desses filmes etc.

A partir disso, mostra-se um grafo interativo na tela para que o<br>
usuário possa visualizar:<br>
1 - Os 15 filmes mais recentes que o ator/a atriz pesquisada(o) participou;<br>
2 - que outros atores/atrizes participaram desses filmes etc.<br>

**Backend**:<br>
    - Linguagem: Python<br>
    - Framework: [FastAPI](https://fastapi.tiangolo.com/)<br>
    - Bibliotecas: [ImdbPy](https://imdbpy.github.io/)<br>

**Frontend**:<br>
    - Linguagem: Javascript<br>
    - Framework: [VueJs](https://vuejs.org/)<br>


### Grafos & escolha do tema

O tema escolhido (filmes e atores/atrizes) foi escolhido por se encaixar adequadamente ao conceito de grafos: A partir de um ator podemos encontrar quais os filmes em que ele trabalhou, e a partir dos filmes encontrar outros atores que atuaram nesses filmes, resultando numa estrutura de grafo direcionado e bipartido. As arestas significam que determinado ator (from)participou de determinado filme (to), sendo que cada nó é um ator/atriz ou um filme.

<hr>

## Screenshots

__Tela inicial__
![](img/cinegraph_home.png)

__Tela de pesquisa__
![](img/cinegraph_search.png)

__Tela de resultados exibindo o grafo montado__
![](img/cinegraph_graph.png)

<hr>

## Instalação 

### Requisitos para utilizar esse projeto

- conexão de internet;<br>
- navegador web de escolha livre;<br>
- terminal/console/shell no computador;<br>
- npm;<br>
- docker & docker-compose;<br>
- clonar o projeto;

> Para clonar o projeto digite:

    git clone https://github.com/projeto-de-algoritmos/Grafos1_Top.git

### Instalando o backend

Tenha a certeza de ter o [docker](https://docs.docker.com/get-docker/) e o [docker compose](https://docs.docker.com/compose/) instalados e em execução. Você pode verificar a instalação de ambos com os seguintes comandos:

    docker --version

E 

    docker-compose --version


Caso ambos estejam corretamente instalados você deve obter uma saída parecida com:

> Note que a sua versão pode ser diferente da exibida abaixo.

![](img/docker_version.png)

Na sequência, considerando que você está na raiz do projeto, digite

    cd backend/

Para ir até a pasta do backend, e na sequência inicie a API com o comando

    (sudo) make up

> O sudo é opcional a depender de como você configurou o docker.

Caso nenhum erro ocorra você terá uma tela parecida com a abaixo:

![](img/back_tuto.png)


### Instalando o frontend

Para o front é necessário ter instalado o [node & npm](https://nodejs.org/en/).

Caso você esteja na raiz do projeto vá até a pasta do front-end digitando num terminal:

    cd frontend

E instale as dependências necessárias com o comando:

    npm install

Após a instalação das dependências inicie o projeto:

    npm run serve

Caso tudo ocorra com sucesso você terá uma tela parecida com a abaixo:

![](img/front_tuto.png)

<hr>

## Uso

Antes de usar, faça a [instalação](#Instalação) do projeto.

1. Abra o navegador web de sua escolha;<br>
2. Digite na barra de busca o endereço informado pelo frontend (por padrão `http://localhost:8080/` caso você não tenha nenhuma outra aplicação utilizando essa porta);
3. (Opcional) Escolha o limite de atores que devem ser retornados por filme (8 por padrão);
4. Na barra de pesquisa da página, digite o nome de um ator ou de uma atriz;<br>
5. Selecione uma (1) das opções mostradas e clique nela<br>
6. Aguarde alguns segundos, o software está preparando o grafo<br>
(isso pode demorar um pouco)<br>
6.1 Essa parte porde demorar mais do que um minuto pelo fato de a aplicação fazr webscrapping em diversas páginas do Imdb então seja paciente!
7. Interaja livremente com o grafo !<br>

- Para mover o grafo simplesmente segure e arraste em qualquer direção dentro do espaço em que se encontra o grafo após o mesmo ser carregado.

- É possível dar zoom no grafo: simplesmente use o scroll do mouse na parte interna do espaço em que se encontra o grafo.

- Caso queira ver mais detalhes sobre um filme simplesmente clique no nó correspondente. Uma tela com detalhes irá aparecer à esquerda.
<hr>

## Problemas ? Sugestões ?

Caso você tenha alguma dificuldade, sugestão ou algum problema com o projeto,<br>
por favor entre em contato conosco:

- Elias Bernardo - ebmm01@gmail.com - telegram @ebmm01
- Erick Giffoni - giffoni.erick@gmail.com - telegram @ErickGiffoni<br>




