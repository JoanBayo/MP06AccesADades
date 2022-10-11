from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

template = environment.get_template("LaMevaVida.html")

# VARIABLES QUE POSEM AL TEMPLATE
info = {"titol":"La meva vida"}

contingut = template.render(info)
# FITXER FINAL ON APLIQUEM LES DADES I AGAFEM LA BASE DEL HTML
file = open("LaMevaVida.html","w")
# ESCRIVIMEL CONTINGUT FINAL
file.write(contingut)