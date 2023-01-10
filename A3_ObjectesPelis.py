import pickle

print("Creador i lector de objectes Pelis:")


class pelis:
    def __init__(self, titol, director, duracio, puntuacio, genere):
        self.titol = titol
        self.director = director
        self.duracio = duracio
        self.puntuacio = puntuacio
        self.genere = genere


titol = input("Títol: ")
director = input("Director: ")
duracio = input("Duració: ")
puntuacio = input("Puntuació: ")
genere = input("Genere: ")


peli = pelis(titol, director, duracio, puntuacio, genere)

with open ("pelis.pickle", "ab") as fichero:
    pickle.dump(peli, fichero)


llistapelis = []
with open ("pelis.pickle","rb") as fichero:
    while True:
        try:
            llistapelis.append(pickle.load(fichero))
        except EOFError:
            break

print("\nLlistat de Pelicules: ")
contador = 1
for p in llistapelis:
    print("\nPelicula " + str(contador) + ":")
    print(p.titul)
    print(p.director)
    print(p.duracio)
    print(p.puntuacio)
    print(p.genere)
    contador += 1

