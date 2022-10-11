import os
import xml.etree.ElementTree as ET

# data//game id//name/year/systems/developer/genre/description/imageURL
existeixDirecotriJocs = os.path.exists("jocs.xml")

if not existeixDirecotriJocs:
    f1 = open("jocs.xml", "w")
    f1.write("<data></data>")
    f1.close()
    # data = ET.fromstring("<data></data>")
    # tree = ET.ElementTree(data)
    # tree.write("jocs.xml")
tree = ET.parse("jocs.xml")
root = tree.getroot()

#
# else:
#     tree = ET.parse("jocs.xml")
#     data = tree.getroot()

while (True):
    # Introduim lindex amb les diferentes opcions
    print("1- Insertar un nou joc")
    print("2- Llistar els jocs (id, name, year, developer)")
    print("3- Mostrar totes les dades de un joc")
    print("4- Modificar un joc")
    print("5- Eliminar un joc")
    print("6- Soritr")

    resposta: int = int(input("Introdueix una opció: "))

    if resposta == 6:
        print("Andusiauu!")
        break

    if resposta == 1:
        # Fer un bucle per trobar el ID del ultim element
        contadorJocs = 0
        for element in root.findall('game'):
            id = element.get('id')
            if int(id) > contadorJocs:
                contadorJocs = int(id)
        contadorJocs += 1

        name = input("Quin és el nom del joc? ")
        year = input("Quin any és va crear? ")
        system = input("En quina plataforma és juga? ")
        developer = input("Qui el va crear? ")
        genre = input("Quin genere de joc és? ")
        description = input("Fes una breu descripcio del joc: ")
        imageURL = input("Posa la URL de una imatge relacionada amb el joc: ")

        idJoc = str(contadorJocs)
        game = ET.Element("game")
        nom = ET.SubElement(game, "name")
        nom.text = name
        any = ET.SubElement(game, "year")
        any.text = year
        sistema = ET.SubElement(game, "system")
        sistema.text = system
        desenvolupador = ET.SubElement(game, "developer")
        desenvolupador.text = developer
        genere = ET.SubElement(game, "genre")
        genere.text = genre
        descripcio = ET.SubElement(game, "description")
        descripcio.text = description
        imatge = ET.SubElement(game, "imageURL")
        imatge.text = imageURL
        game.set("id", idJoc)
        root.append(game)
        tree.write("jocs.xml")

    if resposta == 2:
        for element in root.findall('game'):
            id = element.get('id')
            nom = element.find('name').text
            any = element.find('year').text
            desenvolupador = element.find('developer').text
            print("ID:", id, "  Nom:", nom, "  Any:", any, "  Desenvolupador:", desenvolupador)
        print()

    if resposta == 3:
        mostraTotsElements = input("Posa la ID del joc que vulguis veure totes dels dades: ")
        for element in root.findall('game'):
            if mostraTotsElements == element.get('id'):
                id = element.get('id')
                nom = element.find('name').text
                any = element.find('year').text
                sistema = element.find('system').text
                desenvolupador = element.find('developer').text
                genere = element.find('genre').text
                imatge = element.find('imageURL').text

        print("ID: ", id, "\nNom: ", nom, "\nAny: ", any, "\nSistema: ", sistema, "\nDesenvolupador: ", desenvolupador,
              "\nGenere: ", genere, "\nImatgeURl: ", imatge, "\n\n")

    if resposta == 4:
        idJocBorrar = input("Posa la ID del joc que vols modificar: ")

        for element in root.findall('game'):
            if idJocBorrar == element.get('id'):
                root.remove(element)
                print("Introduiex les noves dades: ")
                name = input("Quin és el nom del joc? ")
                year = input("Quin any és va crear? ")
                system = input("En quina plataforma és juga? ")
                developer = input("Qui el va crear? ")
                genre = input("Quin genere de joc és? ")
                description = input("Fes una breu descripcio del joc: ")
                imageURL = input("Posa la URL de una imatge relacionada amb el joc: ")

                idJoc = str(idJocBorrar)
                game = ET.Element("game")
                nom = ET.SubElement(game, "name")
                nom.text = name
                any = ET.SubElement(game, "year")
                any.text = year
                sistema = ET.SubElement(game, "system")
                sistema.text = system
                desenvolupador = ET.SubElement(game, "developer")
                desenvolupador.text = developer
                genere = ET.SubElement(game, "genre")
                genere.text = genre
                descripcio = ET.SubElement(game, "description")
                descripcio.text = description
                imatge = ET.SubElement(game, "imageURL")
                imatge.text = imageURL
                game.set("id", idJoc)
                root.append(game)
                tree.write("jocs.xml")

    if resposta == 5:
        idJocBorrar = input("Posa la ID del joc que vols eliminar: ")
        for element in root.findall('game'):
            if idJocBorrar == element.get('id'):
                root.remove(element)

        tree.write("jocs.xml")
