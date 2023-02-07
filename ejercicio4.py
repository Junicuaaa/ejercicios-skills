""" 4. Que son las expresiones regulares en Python? """
"""
También pueden ser llamadas regex, son unas secuencias de carácteres los cuales forman un patron de búsqueda.
las expresiones regulares pueden incluir patrones de coincidencia literal, de composición, repetición, ramificación y otras
sofisticadas relgas de reconocimiento de texto 
"""
import re

texto ="hago parte de Campus programmers land"
palabraClave = "campus"


if re.search(palabraClave.upper(), texto.upper()) is not None:
    print("he encontrado la palabra")
else:
    print("no he encontrado la palabra")