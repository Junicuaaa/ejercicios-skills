def detector_edad ():
    edad = int(input(
        "Ingrese su edad \n ->"
    ))
    if edad < 18 and edad%2 == 0:
        print("tu edad es un número par y eres menor de edad aún")
    elif edad > 18 and edad%2 == 0:
        print("tu edad es un número par y eres mayor de edad")
    elif edad > 18 and edad%2 != 0:
        print("tu edad es un numero impar pero eres mayor de edad")
    else: print("tu edad es un numero impar y eres menor de edad :(")
    
        


detector_edad()