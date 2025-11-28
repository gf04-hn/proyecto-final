import random
import string

ARCHIVO = "contraseñas_guardadas.txt"


def generar_letras(longitud):
    return ''.join(random.choice(string.ascii_letters) for _ in range(longitud))

def generar_numeros(longitud):
    return ''.join(random.choice(string.digits) for _ in range(longitud))

def generar_letras_numeros(longitud):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def generar_completa(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))


def leer_contraseñas():
    try:
        with open(ARCHIVO, "r") as f:
            lineas = f.readlines()
            return [linea.strip().split(": ")[1] for linea in lineas]
    except FileNotFoundError:
        return []


def generar_no_repetida(funcion_generadora, longitud):
    existentes = leer_contraseñas()

    while True:
        nueva = funcion_generadora(longitud)
        if nueva not in existentes:
            return nueva



def guardar_en_txt(nombre_app, contraseña):
    with open(ARCHIVO, "a") as archivo:
        archivo.write(f"{nombre_app}: {contraseña}\n")


def mostrar_menu():
    print("\n--- GENERADOR DE CONTRASEÑAS ---\n")
    print("\n¿Qué tipo de caracteres quieres usar?\n")
    print("1. Solo Letras")
    print("2. Solo Números")
    print("3. Letras y Números")
    print("4. Completa (Letras, Números y Caracteres Especiales)")
    print("0. Salir\n")


def pedir_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud: "))
            if longitud > 0:
                return longitud
            else:
                print("Debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un número.")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "0":
            print("Saliendo...")
            break

        if opcion not in ["1", "2", "3", "4"]:
            print("Opción incorrecta.")
            continue

        longitud = pedir_longitud()

        print("\n¿Querés generar la contraseña de forma:")
        print("1. Aleatoria (Diferente a las almacenadas)")
        print("2. Manual")
        sub_op = input("Elegí una opción: ")

       
        if opcion == "1":
            generador = generar_letras
        elif opcion == "2":
            generador = generar_numeros
        elif opcion == "3":
            generador = generar_letras_numeros
        else:
            generador = generar_completa


        if sub_op == "1":
            contraseña = generar_no_repetida(generador, longitud)
            print("\nContraseña generada:", contraseña)

        elif sub_op == "2":
            contraseña = input("Ingresá tu contraseña manualmente: ")

        else:
            print("Opción inválida.")
            continue

        app = input("¿Para qué app o sitio es esta contraseña?: ")
        guardar_en_txt(app, contraseña)
        print(" Contraseña guardada en", ARCHIVO)


if __name__ == "__main__":
    main()