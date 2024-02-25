from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

#rota da página inicial
@app.route('/')
def index():
    return render_template("index.html")

#rota da página dos personagens
@app.route('/characters')
def get_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters) #variável que vai trazer as informações em formato de json

    characters = [] #characters vai ser um dicionário

    #um loop para trazer as info. que quero
    for character in dict["results"]:
        character = {
            "name": character["name"],
            "species": character["species"],
            "gender": character["gender"],
            "origin": character["origin"],
            "location": character["location"]

        }

        #adicionando na lista
        characters.append(character)

    return render_template("characters.html", characters=dict["results"])

#rota da página das localizações
@app.route('/locations')
def get_locations():
    url = "https://rickandmortyapi.com/api/location/"
    response = urllib.request.urlopen(url)
    locations = response.read()
    dict = json.loads(locations) 

    locations = [] 
    #um loop para trazer as info. que quero, no caso, só o nome do personagem
    for location in dict["results"]:
        location = {
            "name": location["name"],
            "type": location["type"],
            "dimension": location["dimension"]

        }

        #adicionando na lista
        locations.append(location)

    return render_template("locations.html", locations=dict["results"])

#rota da página dos episódios
@app.route('/episodes')
def get_episodes():
    url = "https://rickandmortyapi.com/api/episode/"
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes) 

    episodes = [] 
    #um loop para trazer as info. que quero, no caso, só o nome do personagem
    for episode in dict["results"]:
        episode = {
            "name": episode["name"],
            "air_date": episode["air_date"],
            "episode": episode["episode"],
            "characters": episode["characters"]

        }

        #adicionando na lista
        episodes.append(episode)

    return render_template("episodes.html", episodes=dict["results"])

#rota da página do perfil da localização
@app.route('/locations/<id>/')
def get_locations_id(id):
    url = "https://rickandmortyapi.com/api/location/" + id
    response = urllib.request.urlopen(url)
    location_info = response.read()
    dict = json.loads(location_info) 

    location_id = {
        "name": dict["name"],
        "type": dict["type"],
        "dimension": dict["dimension"],
        "residents": dict["residents"]
    }

    return render_template("location.html", location_id=location_id)

#rota da página do perfil do episódio
@app.route('/episode/<id>')
def get_episodes_id(id):
    url = "https://rickandmortyapi.com/api/episode/" + id
    response = urllib.request.urlopen(url)
    episodes_id = response.read()
    dict = json.loads(episodes_id) 

    return render_template("episode.html", episodes_id=dict)

#rota da página do perfil da localização
@app.route('/profile/<id>')
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    profile = response.read()
    dict = json.loads(profile) 

    return render_template("profile.html", profile=dict)



if __name__ == "__main__":
    app.run(port=5000, debug=True)