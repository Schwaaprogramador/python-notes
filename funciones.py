#Las funciones Build-in son como decir, las funciones nativas de python


#Encontrando el numero mayor de una lista.
numeros = [ 3, 2 , 1,5,15]
numero_mas_alto = max(numeros) 
print(numero_mas_alto)



#Mas funciones nativas
    #min() - el parametro tiene que ser una lista de numeros.
    #round() - recibe dos parametros, el numero y los decimales para reondear.
    #bool() - convierte el parametro en un booleano. Si esta vacio, devuelve false. 0=> false
    #all() - si todos los valores son verdaderos, retorna true.
    


#Como crear una funcion.
#Se utiliza un def
def nombre_de_funcion():
    print("funcion creada")
    

nombre_de_funcion()

#Se le pueden pasar parametros normal como en JS
def ejemplo(parametro):
    print(parametro)
    
    
ejemplo('hola')
ejemplo('pepe')