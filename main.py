# Juego de adivina el número.
import random

def generate_random_number():                   # creo la funcion que me va a dar un numero aleatorio
    random_number = random.randint(1, 100)      # generamos un numero aleatorio del 1 al 100 y lo meto dentro de una variable
    return random_number                        # pido que me devuleva ese nnumero que he generado


def ask_user_number(aviso = "Guess the number: "):  # creo la funcion mediante la cual el usuario me proprcionara un numero
    user_number = int(input(aviso))                 # creo la variable que va a contener el numero elegido por el usuario
    return user_number                              # pido que me devuelva el numero del usuario




def check_user_number(user_number, random_number): #creo la funcion con la que voy a manipular las posibilidades que tiene el numero elegido por el usuario
    if user_number <= 0 or user_number > 100:
        return "Null"                               # si el numero es 0, un numero negativo o superior a 100 sera nulo
    if user_number > random_number:             

        return "Too high"                           # si el numero es mayor que el seleccionado por la maquina te devolvera el mensaje de que es demasiado alto
    elif user_number < random_number:
        return "Too low"                             # si el numero es mayor que el seleccionado por la maquina te devolvera el mensaje de que es demasiado bajo
    else:
        return "congratulations"                     # si el numero no cumple ninguna de las condiciones anteriores, enhorabuena, has acertado!

def executor():
    user_congratuled = False                                    
    start = True                                                        
    while user_congratuled or start:                                    # si se cumple una de las dos variables declaradas antes
        random_number = generate_random_number()                        # el ordenador elige un nnumero al azar del 1-100
        user_number = ask_user_number()                                 # el usuario selecciona su numero
        aviso = check_user_number(user_number, random_number)           # y dependiendo de los numeros elegidos la consola te indicara
        while aviso != "congratulations":                               # mientras no des con el numero correctto
            print(aviso)                                                # la cosola te dira que sigas intentandolo   
            user_number = ask_user_number("Try again: ")                        
            aviso = check_user_number(user_number, random_number)           
        print(aviso)                                                        
        user_congratuled = True                                                
executor()                                                                                  
