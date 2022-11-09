import os
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import urllib.request

from extreureInfoDelFeed import extreureInfoDelFeed

existeixDirecotriPodcasts = os.path.exists("Podcasts.xml")

if not existeixDirecotriPodcasts:
    f1 = open("Podcasts.xml", "w")
    f1.write("<data></data>")
    f1.close()
tree = ET.parse("Podcasts.xml")
root = tree.getroot()




while (True):
    # Introduim lindex amb les diferentes opcions
    print("1- Insertar un nou feed")
    print("2- Llistar els feeds")
    print("3- Eliminar un feed")
    print("4- Crear una pagina Web amb la informació dels Podcasts")
    print("5- Sortir")

    resposta = int(input("Introdueix una opció: "))

    if resposta == 5:
        print("Andusiauu!")
        break

    if resposta == 1:
        # Fer un bucle per trobar el ID del ultim element
        contadorPodcasts = 0
        for element in root.findall('podcast'):
            id = element.get('id')
            if int(id) > contadorPodcasts:
                contadorPodcasts = int(id)
        contadorPodcasts += 1

        name = input("Quin és el nom del Podcast? ")
        feed = input("Introdueix el feed del Podcast? ")


        idPodcast = str(contadorPodcasts)
        podcast = ET.Element("podcast")
        nom = ET.SubElement(podcast, "name")
        nom.text = name
        feeds = ET.SubElement(podcast, "feed")
        feeds.text = feed
        podcast.set("id", idPodcast)
        root.append(podcast)
        tree.write("Podcasts.xml")

    if resposta == 2:
        for element in root.findall('podcast'):
            id = element.get('id')
            nom = element.find('name').text
            feeds = element.find('feed').text
            print("ID:", id, "  Nom:", nom, "  Feed:", feeds)
            print("      -----------------------------------------------------")
        print()


    if resposta == 3:
        idBorrarPodcasts = input("Posa la ID del joc que vols eliminar: ")
        for element in root.findall('podcast'):
            if idBorrarPodcasts == element.get('id'):
                root.remove(element)

    if resposta == 4:
        environment = Environment(loader=FileSystemLoader("templatesPodcasts/"))
        template = environment.get_template("plantillaWebPodcasts.html")

        dadesPodcast = []

        for element in root.findall('podcast'):
            feeds = element.find('feed').text
            url = feeds
            connexio = urllib.request.urlopen(url)
            contingut = connexio.read().decode('UTF-8')
            diccionariPodcast = extreureInfoDelFeed(contingut)
            dadesPodcast.append(diccionariPodcast)

        info = {"podcasts": dadesPodcast}
        contingut = template.render(info)
        file = open("llistaPodcasts.html", "w")
        file.write(contingut)
        file.close()
        # info = {"podcasts": dadesPodcast}
        # contingut = template.render(info)
        # file = open("PodcastAddiction/templatesPodcasts/llistatPodcasts.html","w")
        # file.write(contingut)


