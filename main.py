from data import people

def list_user():
    if not people:
        print("El directorio está vacío")
    else:
        for nombre, numero in people.items():
            print(f"Nombre: {nombre} Número: {numero} \n +\n")

def add_user():
    nombre = input("Ingrese el nuevo nombre: ")
    numero = input("Ingrese el nuevo número de teléfono: ")
    if nombre and numero in people:
        print("El cliente ya existe")
    else:
        people.append({"Nombre": nombre, "Número": numero})
    print(f"Usuario {nombre} agregado exitosamente.")

 