![Capa](./assets/Carmen-Portinho.png)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Índice <a name="retornar-ao-índice"></a>
- [Consumo de API com Flask](#consumo)
- [Enunciado](#enunciado)
- [Resolução](#resolucao)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Consumo de API com Flask<a name="consumo"></a>
> O seriado Rick and Morty é um desenho animado americano de comédia e ficção científica criado por Justin Roiland e Dan Harmon para o bloco de programação noturno Adult Swim, exibido no canal Cartoon Network. A série acompanha as perigosas aventuras do cientista louco Rick e seu neto Morty, que divide seu tempo entre a vida familiar e
viagens interdimensionais. A série é inspirada em Back to the Future e Doctor Who.

<div style="text-align:center">
    <img src="./assets/RickAndMorty.gif" width="300px" alt="Rick and Morty">
</div>

A API do Rick and Morty é uma API pública que contém informações sobre os personagens da série. A documentação da API pode ser encontrada neste [link](https://rickandmortyapi.com/documentation/#rest).

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Enunciado<a name="enunciado"></a>

> A API possui três endpoints: um para listar os personagens, um para listar as localizações e dimensões e um para listar os episódios. O objetivo deste exercício é adicionar novas funcionalidades ao projeto.

1. `GET` `/locations` - Criar uma nova rota para listar as localizações.
    - A página deverá ser renderizada através do template locations.html.
    - A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão.
    - A tabela deverá conter um link para a página de perfil da localização.
2. `GET` `/episodes` - Criar uma nova rota para listar os episódios.
    - A página deverá ser renderizada através do template episodes.html.
    - A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código.
    - A tabela deverá conter um link para a página de perfil do episódio.
3. `GET` `/location/<id>` - Criar uma nova rota para exibir o perfil da localização.
    - A página deverá ser renderizada através do template location.html.
    - A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os personagens que aparecem na
    localização.
    - A lista deverá conter um link para a página de perfil
    do personagem.
4. `GET` `/episode/<id>` - Criar uma nova rota para exibir o perfil do episódio.
    - A página deverá ser renderizada através do template episode.html.
    - A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que
    aparecem no episódio.
    - A lista deverá conter um link para a página de perfil do personagem.
5. Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. As informações de origem, localização e episódios em que o personagem aparece devem conter um link para a página de perfil da localização.

[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Resolução<a name="resolucao"></a>

Os exercícios foram resolvidos em grupo através de chamadas via Discord e organizados de acordo com um quadro Kanban no Trello:

![trello](./assets/Trello.png)

Nas reuniões indentificávamos o que era preciso ser feito e criávamos as tarefas de acordo com o que foi discutido.



[![Retornar ao índice](https://img.shields.io/badge/Retornar%20ao%20%C3%ADndice-Verde%20Escuro?color=%23006400&style=flat&labelColor=%23006400&logo=github)](#retornar-ao-índice)

## <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px;"/> Integrantes <a name="integrantes"></a>

<div style="align-itens:center">
<table>
  <tr>
    <td><a href="https://github.com/alynebrasil"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/37218646?v=4" width="100px;" alt="Imagem Alyne"/><br /><sub><b>Alyne Brasil</b></sub></a><br /><a href="https://github.com/alynebrasil">👩‍💻</a></td>
    <td><a href="https://github.com/anamariagds"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/23744957?v=4" width="100px;" alt="Imagem Ana Maria"/><br /><sub><b>Ana Maria Gomes</b></sub></a><br /><a href="https://github.com/anamariagds">👩‍💻</a></td>
    <td><a href="https://github.com/cibelemoraes"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/93668580?v=4" width="100px;" alt="Imagem Ana Maria"/><br /><sub><b>Cibelle Moraes</b></sub></a><br /><a href="https://github.com/cibelemoraes">👩‍💻</a></td>
    <td><a href="https://github.com/danisoaresl"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/84364512?v=4" width="100px;" alt="Imagem Daniele"/><br /><sub><b>Daniele Soares</b></sub></a><br /><a href="https://github.com/danisoaresl">👩‍💻</a></td>
    <td><a href="https://github.com/gabiapp"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/108434852?v=4" width="100px;" alt="Imagem Gessyca"/><br /><sub><b>Gabriela Nunez</b></sub></a><br /><a href="https://github.com/gabiapp">👩‍💻</a></td>
    </tr>
    <tr>
    <td><a href="https://github.com/GessycaBorges"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/124705468?v=4" width="100px;" alt="Imagem Gessyca"/><br /><sub><b>Gessyca Borges</b></sub></a><br /><a href="https://github.com/GessycaBorges">👩‍💻</a></td>
    <td><a href="https://github.com/OrcFofa"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/104779345?v=4" width="100px;" alt="Imagem Laura"/><br /><sub><b>Laura Santos</b></sub></a><br /><a href="https://github.com/OrcFofa">👩‍💻</a></td>
    <td><a href="https://github.com/liviazeviani"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/66968738?v=4" width="100px;" alt="Imagem Lívia"/><br /><sub><b>Lívia Zeviani</b></sub></a><br /><a href="https://github.com/liviazeviani">👩‍💻</a></td>
    <td><a href="https://github.com/Renatarafaelaalves"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/141291179?v=4" width="100px;" alt="Imagem Renata"/><br /><sub><b>Renata Rafaela Alves</b></sub></a><br /><a href="https://github.com/Renatarafaelaalves">👩‍💻</a></td>
    <td><a href="https://github.com/thaynarlt"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/75785465?v=4" width="100px;" alt="Imagem Thayna"/><br /><sub><b>Thayná Tolentino</b></sub></a><br /><a href="https://github.com/thaynarlt">👩‍💻</a></td>
  </tr>
</table>
</div>