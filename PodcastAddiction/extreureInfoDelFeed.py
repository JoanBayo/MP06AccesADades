import os
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader
import urllib.request


def extreureInfoDelFeed(contingut):
    # <channel>
    #     <title>
    #     <link>
    #     <itunes:image>
    #     <item>
    #         <title>
    #         <link>
    #         <description>
    #         <itunes:duration>
    #         <itunes:image>
    #         <enclosure url=>
    tree = ET.fromstring(contingut)

    for element in tree.findall('channel'):

        try:
            titul = element.find('title').text
        except:
            titul = ""

        try:
            links = element.find('link').text
        except:
            links = ""

        try:
            itunesImage = element.find('image').find('url').text
        except:
            itunesImage = ""

        try:
            titulEpisodi = element.find('item').find('title').text
        except:
            titulEpisodi = ""

        try:
            linksEpisodi = element.find('item').find('link').text
        except:
            linksEpisodi = ""

        try:
            duracio = element.find('item').find('pubDate').text
        except:
            duracio = ""

        try:
            imatge = element.find('image').find('url').text
        except:
            imatge = ""

        try:
            descripcio = element.find('item').find('description').text
        except:
            descripcio = ""

        try:
            descaregar = element.find('item').find('enclosure').attrib['url']
        except:
            descaregar = ""



        diccionariPodcast = {"titul": titul, "links": links, "itunesImage": itunesImage,
                             "titulEpisodi": titulEpisodi,"linksEpisodi": linksEpisodi,
                             "duracio":duracio ,"imatge": imatge,"descripcio":descripcio ,
                             "descaregar":descaregar}
        return diccionariPodcast


    # environment = Environment(loader=FileSystemLoader())
    # template = environment.get_template("passarInformacio.html")
    #
