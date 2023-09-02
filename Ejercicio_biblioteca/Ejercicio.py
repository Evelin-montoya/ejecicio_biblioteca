##Primera funcion evelin

# Registro de libro
libro = []

# Registro de un nuevo usuario
def registrar_libros ():
    isbn = input("Ingrese el ibsn: ")
    nombre = input("Nombre: "),
    autor = input("Autor: "),
    num_paginas = input("Número de paginas: ")
    año_publicacion = input("Año de publicación: ")
    libro.append({"Ingrese el ibsn": isbn,"Nombre": nombre, "Autor": autor, "Número de paginas": num_paginas, "Año de publicación":año_publicacion})
    print("Registro exitoso.")


print(registrar_libros())


#funcion kelly