import os.path
import shutil
import urllib.request
from getpass import getuser


def actualitzarFitxer():
    urlActualitzar = input("Posa la URL a actualitzar: ")
    Fitxer = comprovarPathDomini(urlActualitzar) + "/" + finalPathFitxer(urlActualitzar) + ".html"

    if os.path.exists(Fitxer):
        # BORREM LA CARPETA
        shutil.rmtree(comprovarPathDomini(urlActualitzar))
        # GENEREM LA CARPETA
        generarCarpeta(urlActualitzar)
        # CREEM EL FITXER
        generarFitxer(urlActualitzar)
        print("URL actualitzada correctament")

    else:
        print("Aquesta URL no existeix i per tant no es pot actualitzar")


def descarregarURL():
    urlDescarregar = input("Posa la URL a descarregar: ")
    # MIREM SI EL FITXER EXISTEIX

    if existeixFitxer(urlDescarregar):
#COPIAR FITXER
        fitxerActual = open(comprovarPathDomini(urlDescarregar) + "/" + finalPathFitxer(urlDescarregar) + ".html")
        fitxerNou = open(comprovarPathDomini(urlDescarregar) + "/" + finalPathFitxer(urlDescarregar) + "-OLD-" + valorOLD(urlDescarregar) + ".html", "w")
#ESCIRURE EL FITXER
        fitxerNou.write(fitxerActual.read())
        fitxerActual.close()
        fitxerNou.close()
#BORRAR FITXER ANTIC
        os.remove(comprovarPathDomini(urlDescarregar) + "/" + finalPathFitxer(urlDescarregar) + ".html")

        print("El fitxer '" + finalPathFitxer(urlDescarregar) + ".html' s'ha actualitzat amb el nom: '" + finalPathFitxer(urlDescarregar) + "-OLD-" + valorOLD(urlDescarregar) + ".html")
        generarFitxer(urlDescarregar)
        print("S'ha creat el fitxer '" + finalPathFitxer(urlDescarregar) + ".html'")
        print()
# SI EL FITXER NO EXISTEIX
    else:
#CREAR CARPETA
        generarCarpeta(urlDescarregar)
        print("Aquest fitxer no existeix, per tant generem una nova carpeta '" + urlDescarregar.split("/")[2]+"'")

        generarFitxer(urlDescarregar)
        print("I també generem el fitxer: '" + finalPathFitxer(urlDescarregar) + ".html'")


def existeixFitxer(url):
    pathFitxer = comprovarPathDomini(url) + "/" + finalPathFitxer(url) + ".html"
    # RETORNEM SI EL PATH EXISTEIX
    return os.path.exists(pathFitxer)


def comprovarPathDomini(url):
    global dominiMeu
    carpetaSeparada = url.split("/")
    #COMPROVEM SI ES UNA URL
    try:
        dominiMeu = carpetaSeparada[2]
    except:
        print("Aquesta URL no és correcta")

    path = "/home/" + getuser() + "/URLDownloaderJoanBayo/" + dominiMeu
    return path


def finalPathFitxer(url):
#DEFINIM EL PATH FINAL DEL FITXER
    finalPathFitxer = url.split("/")
    numeroFinalPath = (len(finalPathFitxer) -1)
    finalPathFitxer = finalPathFitxer[numeroFinalPath]
    return (finalPathFitxer)



def valorOLD(url):
#COMPROVEM ELS ALTRES FITXERS PER MIRAR EL VALOR ASSIGNAR
    valorOLD = 1
    while True:
        FitxerOLD = comprovarPathDomini(url) + "/" + finalPathFitxer(url) + "-OLD-" + str(valorOLD) + ".html"
        if not os.path.exists(FitxerOLD):
            return str(valorOLD)
        valorOLD += 1


def generarFitxer(url):
    Fitxer = comprovarPathDomini(url) + "/" + finalPathFitxer(url) + ".html"
    connexio = urllib.request.urlopen(url)
    contingut = connexio.read().decode('UTF-8')

    if not existeixFitxer(url):
        WriteFitxer = open(Fitxer, "w")
        WriteFitxer.write(contingut)
        WriteFitxer.close()


def generarCarpeta(url):
    CarpetaPrograma = "/home/" + getuser() + "/URLDownloaderJoanBayo"
    existeixCarpetaPrograma = os.path.exists(CarpetaPrograma)

    # CREEM LA CARPETA SI NO EXISTEIX
    if not existeixCarpetaPrograma:
        os.mkdir(CarpetaPrograma)

    # DEFINIM EL PATH DE LA CARPETA DEL DOMINI
    CarpetaDomini = comprovarPathDomini(url)
    existeixCarpetaDomini = os.path.exists(CarpetaDomini)

    # CREEM LA CARPETA SI NO EXISTEIX
    if not existeixCarpetaDomini:
        os.mkdir(CarpetaDomini)


while True:
    print("URL DOWNLOADER")
    print("1- Sortir del programa")
    print("2- Descarregar URL")
    print("3- Actualitzar URL")
    opcio = int(input("Que vols fer: "))

    if opcio == 1:
        print("Andusiauuu!")
        break

    if opcio == 2:
        descarregarURL()

    if opcio == 3:
        actualitzarFitxer()