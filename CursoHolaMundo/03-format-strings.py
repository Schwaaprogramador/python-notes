
#Operador de formateo de String. La f inicial antes de la cadena
nombre = "Schwaa"
apellido = "Pepe"
nombre_completo = nombre + " " + apellido
nombre_completo2 = f"{nombre} {apellido}"
print(nombre_completo2)



#Metodos de strings
print(nombre.upper())   #Todo a mayuscula.
print(nombre.lower())   #Todo a minuscula.
print(nombre.capitalize())   #Primer caracter en mayuscula.
print(nombre.title())   #Todas las palabras con Mayuscula.
print(nombre.strip())   #Remover los espacios.

print(nombre.find("waa"))   #Encuentra el indice. -1 No encontro.
print(nombre.replace("waa", "pepe")) 