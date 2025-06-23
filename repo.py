
def datos_Adan():
    print("Mi nombre es Adán Valdebenito y tengo 22 años")

def datos_Juan_Arellano() :
    print("Mi nombre es Juan Arellano y tengo 38 años.")


def datos_benjamin_morales():
    print("Mi nombre es Benjamín Morales y tengo 34 años.")

# Menú base del programa

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Función de integrante 1")
    print("2. Función de integrante 2")
    print("3. Función de integrante 3")
    print("4. Función de Juan Arellano")
    print("0. Salir")
    op = input("Seleccione opción: ")
    if op == "0":
        print("Programa finalizado.")
        break
    elif op == "1":
        pass def datos_Aman():
            print("Mi nombre es Amán Fernández y tengo 23 años 👁️👄👁️")
    elif op == "2":
        datos_Adan()
    elif op == "3":
        datos_benjamin_morales()
        pass # Aquí se llamará a la función del integrante 3
    elif op == "4":
        datos_Juan_Arellano()
    else:
        print(" Opción inválida.")
