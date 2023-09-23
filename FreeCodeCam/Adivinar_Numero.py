#Mayor, menor o igual
#Recordar que la funcion input siempre retorna una cadena de caracteres. Por lo que toca formatearlo.
import random #Se importa de python nativo

def adivina_el_numero(numero_maximo):
    
    print('===============================')
    print('Bienvenido')
    print('===============================')
    print('Adivina el numero')
    
    numero_aleatorio = random.randint(1, numero_maximo) #Numero aleatorio entre 1-x.
    prediccion = 0 
    
    while prediccion != numero_aleatorio:
        
        prediccion = input(f"Adivina un numero entre 1 y {numero_maximo}: ") #convertir a numero
        prediccion_Integrada = int(prediccion)
        #print(type(prediccion_Integrada))
        
        if prediccion_Integrada < numero_aleatorio:
            print("Intenta otra vez. Numero muy pequeno.")
        elif prediccion_Integrada > numero_aleatorio:
            print("Intenta otra vez. Numero muy grande.")
    
    print('Has adivinado el numero')
        

adivina_el_numero(10)