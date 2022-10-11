import shutil
from getpass import getuser
import os
import urllib.request

usuari = getuser()
#Mirem si l'usuari esta creat accedic al directori, mes un getuser
DirectoriUrlGeneral = "/home/" + usuari + "/URLDowloaderBayo"
#Amb el os.path.exists comprovem si el didrectori esta creat, si no ho esta el creem
existeixDirecotriUrlGeneral = os.path.exists(DirectoriUrlGeneral)
if not (existeixDirecotriUrlGeneral):
    os.mkdir(DirectoriUrlGeneral)
    print("S'ha creat un directori nou per treballar\n")
else:
    print("El direcotri amb el que treballaras ja el tens creat\n")
while (True):
    #Introduim lindex amb les diferentes opcions
    print("1. Sortir del programa")
    print("2. Descarregar URL")
    print("3. Actualitzar URL")
    resposta = int(input("Indtrudueix una opció: "))

    if(resposta == 1):
        #Soritm del programa amb un break
        print("Andusiau!")
        break

    if (resposta == 2):

        url = input("Introduiex la URL per descargar: ")
        #Agafem lenllaç i amb el split, aconseguim separar-lo per les barres (/)
        nomUrlSeparada = url.split("/")
        #Creem el direcotri en el qual es guardarar el fitxer, ho fem utilitzan el direcotir creat anteriorment+la segona part de la url separada
        DirectoriUrl= DirectoriUrlGeneral + "/" + nomUrlSeparada[2]
        #fem el mateix que hem fet amb el direcotir anterior, comprovem si existeix i sino el creem
        existeixDirectoriUrl = os.path.exists(DirectoriUrl)
        if not (existeixDirectoriUrl):
            os.mkdir(DirectoriUrl)
        #Ara llegim el link anterior, per accedir al seu HTML i posteriroment printejarlo en un fitxer, amb el nom de la penultima part de la url
        #Agafa el link
        connexio = urllib.request.urlopen(url)
        #EL lletgim amb HTML
        contingut = connexio.read().decode('UTF-8')
        #Creem el nou fitxer amb el nom de la carpeta anterior mes la penultima pert, per aixo fiquem (-1)
        nomFile = DirectoriUrl + "/" + nomUrlSeparada[len(nomUrlSeparada) - 1]
        #comprovem si el fitxer que volem fer ja existeix
        fitxerFinal = nomUrlSeparada[len(nomUrlSeparada)-1].split(".")
        existixFitxer = os.path.exists(nomFile)
        fitxerRenombrat = DirectoriUrl + "/" + fitxerFinal[0] + "OLD-" + str (variableOLD) + "." + fitxerFinal[len(fitxerFinal) -1]
        if (existixFitxer):
            variableOLD = int()
            while (True):
                try:
                    open(nomFile,"x")
                except FileExistsError:
                    variableOLD += 1
                    while os.path.exists(fitxerRenombrat):

                        try:
                            open(DirectoriUrl + "/" + nomUrlSeparada[len(nomUrlSeparada)-1],"x")

                        except FileExistsError:
                            break

                    else:
                        break
                        shutil.copyfile(nomFile, fitxerRenombrat)

            if not os.path.exists(fitxerRenombrat):
                f1 = open(fitxerRenombrat, "w")

            shutil.copyfile(nomFile, fitxerRenombrat)

        if not (existixFitxer):
            f2 = open(nomFile,"w")
            f2 = write(contingut)


        print("fitxer creat")



    if (resposta == 3):
        print("Quina URL vols actualitzar?")
        urlActualitzada = input()
        urlSeparada = urlActualitzada.split("/")
        urlSeparadaFinal = urlSeparada[len(urlSeparada)-1].split(".")
        connexio = urllib.request.urlopen(link)
        contingut = connexio.read().decode("UTF-8")
        if not os.path.exists(nomFile):
            print("Aquest enllaç no esta guardat, i per tan no pot ser modificat")
        else:
            variableOLD = int()
            while (True):
                try:
                    os.remove(nomFile)
                    variableOLD += 1

                    while os.path.exists(fitxerRenombrat):
                        os.remove(fitxerRenombrat)
                        variableOLD += 1

                except Exception:
                    break
                else:
                    break

    if not os.path.exists(nomFile):
        f1 = open(nomFile, "w")
        f1.write(contingut)













