# 14/09/2020
# Dulce Adelina Zuñiga Ramos
# Ejercicio de práctica en clase de graficación

import funciones as f

def realizar_compra():
    f.abrir()

    nombre = input("Escribir el nombre del producto: ")
    cantidad = int(input("Escribe la cantidad: "))

    if(f.verificar_cantidad(nombre,cantidad)):
        f.comprar(nombre,cantidad)
    else:
        print("Intente con otro producto\n")


def agregar():
    f.abrir()

    nombre = input("Escribir el nombre del producto: ")
    precio = float(input("Escribe el precio: "))
    cantidad = int(input("Escribe la cantidad: "))

    f.agregar(nombre,precio,cantidad)
    f.imprimir()
    f.cerrar()

def añadir_cantidad():
    f.abrir()

    nombre = input("Escribir el nombre del producto: ")
    cantidad = int(input("Escribe la cantidad: "))

    f.actualizar_cantidad(nombre, cantidad)
    f.imprimir()
    f.cerrar()

def abrir_cerrar():
    f.abrir()
    f.imprimir()
    f.cerrar()


if __name__ == '__main__':
    #abrir_cerrar('PyCharm')
    #agregar()
    #añadir_cantidad()
    realizar_compra()