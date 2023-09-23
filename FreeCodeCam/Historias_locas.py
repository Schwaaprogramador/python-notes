
#Concatenar cadenas de caracteres.

organizacion = "freeCodeCamp"

print("Aprende a programar con " + organizacion)
print( "Aprende a programar con {}".format(organizacion))
print(f"Aprende a programar con {organizacion}") #f-string


#Mad Libs Historias Locas
adj = input("adj: ")
adj2 = input("adj2: ")
adj3 = input("adj3: ")

madlib = f"Programar es tan {adj}. Arroz con {adj2}. Comere {adj3} "

print(madlib)