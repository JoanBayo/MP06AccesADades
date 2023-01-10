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
            itunesImage = element.find('{http://www.itunes.com/dtds/podcast-1.0.dtd}image').attrib['href']
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
            duracio = element.find('item').find('{http://www.itunes.com/dtds/podcast-1.0.dtd}duration').text
        except:
            duracio = ""

        try:
            imatge = element.find('item').find('{http://www.itunes.com/dtds/podcast-1.0.dtd}image').attrib['href']
        except:
            imatge = ""

        try:
            descripcio = element.find('item').find('{http://www.itunes.com/dtds/podcast-1.0.dtd}summary').text

        except:
            descripcio = element.find('item').find('description').text

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
