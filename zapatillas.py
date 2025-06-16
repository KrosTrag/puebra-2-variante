reservas = {}
zapatillasiniciales = 20

def reservarzapatillas():
    ncomprador = input("Nombre del comprador: ")
    if ncomprador in reservas:
        print("Error: El nombre del comprador ya existe.")
        return

    if len(reservas) >= zapatillasiniciales:
        print("Error: Se ha alcanzado el stock máximo de reservas.")
        return

    clavesecreta = input("Digite la palabra secreta para confirmar la reserva: ")
    if clavesecreta != "EstoyEnListaDeReserva":
        print("Error: Código secreto incorrecto")
        return

    reservas[ncomprador] = 1
    print(f"Reserva realizada exitosamente para {ncomprador}.")

def buscar_zapatillas_reservadas():
    ncomprador = input("Nombre del comprador a buscar: ")
    if ncomprador in reservas:
        paresreservados = reservas[ncomprador]
        tiporeserva = "estándar" if paresreservados == 1 else "VIP"
        print(f"Reserva encontrada: {ncomprador}, {paresreservados} par(es), ({tiporeserva}).")
        pagovip = input("¿Desea pagar adicional para VIP y reservar 2 pares? (si/no): ")
        if pagovip.lower() == "si":
            reservas[ncomprador] = 2
            print("Reserva actualizada a VIP. Ahora", ncomprador, "tiene 2 pares reservados.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")


def canceloreserva():
    ncomprador = input("Nombre del comprador cuya reserva desea cancelar: ")
    if ncomprador in reservas:
        del reservas[ncomprador]
        print(f"La reserva de {ncomprador} ha sido cancelada.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def menu():
    print("TOTEM AUTOATENCIÓN RESERVA STRIKE")
    print("1.- Reservar zapatillas")
    print("2.- Buscar zapatillas reservadas")
    print("3.- Cancelar reserva de zapatillas")
    print("4.- Salir")

def menufinal():
    while True:
        menu()
        opcion = input("Seleccione una opción (1-4): ")
        try:
            opcion = int(opcion)
            if opcion == 1:
                reservarzapatillas()
            elif opcion == 2:
                buscar_zapatillas_reservadas()
            elif opcion == 3:
                canceloreserva()
            elif opcion == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!")
        except ValueError:
            print("Debe ingresar una opción válida!")

menufinal()
