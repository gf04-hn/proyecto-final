import random

tickets = []

def generar_ticket():
    while True:
        print("\nIngrese los datos para Generar un nuevo Ticket")
        nombre = input("Ingrese su Nombre: ")
        sector = input("Ingrese su Sector: ")
        asunto = input("Ingrese Asunto: ")
        mensaje = input("Ingrese un Mensaje: ")

        numero = random.randint(1000, 9999)

        ticket = {
            "nombre": nombre,
            "sector": sector,
            "asunto": asunto,
            "mensaje": mensaje,
            "numero": numero
        }

        tickets.append(ticket)

        print("\n===============================================")
        print("         Se generó el siguiente Ticket")
        print("===============================================")
        print(f"  Su nombre: {nombre}       N°Ticket: {numero}")
        print(f"  Sector: {sector}")
        print(f"  Asunto: {asunto}\n")
        print(f"  Mensaje: {mensaje}\n")
        print("      Recordar su número de Ticket\n")

        r = input("¿Desea generar un nuevo Ticket? (s/n): ").lower()
        if r != "s":
            break


def leer_ticket():
    while True:
        print("\nLectura de Ticket")
        num = input("Ingrese el número de Ticket: ")

        encontrado = False

        for t in tickets:
            if str(t["numero"]) == num:
                print("\n===============================================")
                print("              Ticket Encontrado")
                print("===============================================")
                print(f"  Nombre: {t['nombre']}")
                print(f"  Sector: {t['sector']}")
                print(f"  Asunto: {t['asunto']}")
                print(f"  Mensaje: {t['mensaje']}")
                print(f"  Número: {t['numero']}")
                encontrado = True

        if not encontrado:
            print("\nNo existe ningún ticket con ese número.\n")

        r = input("¿Desea leer otro Ticket? (s/n): ").lower()
        if r != "s":
            break


def menu():
    while True:
        print("\nHola bienvenido al sistema de Tickets\n")
        print("1 - Generar un Nuevo Ticket")
        print("2 - Leer un Ticket")
        print("3 - Salir")
        opcion = input("Seleccione: ")

        if opcion == "1":
            generar_ticket()
        elif opcion == "2":
            leer_ticket()
        elif opcion == "3":
            confirmar = input("¿Está seguro que desea salir? (s/n): ").lower()
            if confirmar == "s":
                print("Programa finalizado.")
                break
        else:
            print("Opción inválida. Intente nuevamente.\n")

menu()