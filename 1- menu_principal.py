def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE PAÍSES ---")
    print("1. Agregar país")
    print("2. Actualizar población/superficie")
    print("3. Buscar país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Estadísticas")
    print("7. Salir")

def ejecutar_menu():
    #paises = cargar_desde_csv("paises.csv") # Función que inicializa la lista
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)
            
        elif opcion == "2":
            actualizar_pais(paises)
            
        elif opcion == "3":
            buscar_pais(paises)
            
        elif opcion == "4":
            filtrar_pais(paises)
            
        elif opcion == "5":
            ordenar_por_pais(paises)
            
        elif opcion == "6":
            estadisticas_por_pais(paises)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            input("Opción inválida, presione ENTER para continuar.")


ejecutar_menu()