""" 9. Construya un algoritmo en Python, que permita ingresar la
información de un empleado e imprima el nombre, los
apellidos y la antigüedad. Los datos que se deben solicitar
son los siguientes:
*Nombre * Teléfono *Año de ingreso a la empresa
*Apellidos *Edad. """

datos_empleado = {
    'Nombre': [], 
    'Telefono': [], 
    'Año_Ingreso': [], 
    'Apellidos': [], 
    'Edad': []
    }

def programa_datos():
    print(
        "Bienvenido al programa para ingresar los datos de sus empleados \n"
        "El orden para ingresar los datos es el siguiente: \n"
        "Nombre \n Telefono \n Año de ingreso \n Apellidos \n Edad."
    )
    o = 0
    while o != 1:
        nombre = str(input("Ingrese el nombre ->"))
        datos_empleado['Nombre'].append(nombre)
        telefono = int(input("Ingrese el telefono ->"))
        datos_empleado['Telefono'].append(telefono)
        año_ingreso = str(input("Ingrese el año de ingreso ->"))
        datos_empleado['Año_Ingreso'].append(año_ingreso)
        apellidos = str(input("Ingrese los apellidos ->"))
        datos_empleado['Apellidos'].append(apellidos)
        edad = int(input("Ingrese la edad ->"))
        datos_empleado['Edad'].append(edad)
        o = int(input("si no quiere ingresar mas empleados y ver los datos presione (1)"))

    for i in datos_empleado:
        for g in datos_empleado.__getitem__(i):
            print(f"{i} : {g}") 

programa_datos()
