def datos_Adan():
    print("Mi nombre es Adán Valdebenito y tengo 22 años")

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("4. Función de integrante 4")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        pass # Aquí se llamará a la función del integrante 1
    elif op == "2":
        datos_Adan()
    elif op == "3":
        pass # Aquí se llamará a la función del integrante 3
    elif op == "4":
        pass # Aquí se llamará a la función del integrante 4
    else:
        print(" Opción inválida.")
