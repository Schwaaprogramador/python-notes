#Se concatena normal como JS
#Las variables se declaran simplemente con =
a = 2
nombre = 'soy'
bienvenida = 'hola ' + nombre + ' mk'
print(bienvenida)

#Los f String, toda la cadena de texto la CONVIERTE a string, para que la variable sin importar el tipo de dato
# dentro del texto funcione.
bienvenida2 = f'hola {nombre} mk'
print(bienvenida2)


#operadores de pertenencia ( in / not in)
nombre2 = 'soy'
print(nombre in nombre2)