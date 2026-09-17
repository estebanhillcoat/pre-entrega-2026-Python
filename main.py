productos = ["kiwi","fideos","pepsi"]

while True:
    opciones = input("Elija la opcion deseada\nR - Remover\nS - Salir\nB - Buscar\nA - Agregar\nL - Listar productos\n")
    
#menu de opciones 

    match opciones:
        case "R":
            producto_remover = input("\nIngrese producto a quitar: \n")
            productos.remove(producto_remover)
            print(f"\n{producto_remover} quitado con exito.\n")
        case "S":
            break
        case "L":
            print(productos)
        case "B":
            producto_a_buscar = input("\nIngrese producto a buscar: \n")
            if producto_a_buscar in productos:
                print(f"{producto_a_buscar} esta en stock")
            else:
                print(f"{producto_a_buscar}, no esta en stock")
