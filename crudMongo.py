from db import Agenda

class crud:
    def insertar(self):
        #Pedimos los datos del contacto a insertar
        id = input("Id: ")
        Nombre = input("Nombre: ")
        Apellido = input("Apellidos: ")
        Telefono = input("Telefono: ")
        contacto = Agenda()
        contacto.insertar(id, Nombre, Apellido, Telefono)

    def modificar(self):
        id = input("Introduce el Id del contacto a modificar: ")
        contacto = Agenda()
        reg = contacto.buscar(id)
        if reg == None:
            print("No existe ningun contacto con ese id")
        else:
            for dato in reg:
                if dato != '_id':
                    print(f'{dato}: {reg[dato]}')
            nombre = input("Introduce nuevo nombre: ")
            apellido = input("Introduce nuevos apellidos: ")
            telefono = input("Introduce nuevo telefono: ")
            contacto.actualizar(id, nombre, apellido, telefono)
            print("Modificar datos")

    def listar(self):
        contacto = Agenda()
        todos = contacto.listar()
        print("L I S T A  D E  C O N T A C T O S") 
        for c in todos:
            print(c)

    def eliminar(self):
        id = input("Introduce el Id del contacto a eliminar: ")
        contacto = Agenda()
        reg = contacto.buscar(id)
        if reg == None:
            print("No existe ningun contacto con ese id")
        else:
            for dato in reg:
                if dato != '_id':
                    print(f'{dato}: {reg[dato]}')
            while True:
                borrar = input("¿Seguro que desea borrar este contacto (S/N)? ")
                if borrar == 's' or borrar == 'S':
                    contacto.eliminar(id)
                    break
                elif borrar == 'n' or borrar == 'N':
                    break
                else:
                    print("Debe respoder [s]i o [n]o")

    def muestra_menu(self):
        #Muestra el menu inicial 
        while True:
            print("[1] Añadir datos")
            print("[2] Actualizar datos")
            print("[3] Listar datos")
            print("[4] Eliminar dato")
            print("[S] Salir\n")
            op = input("Elija una opción ")
            if (op == "1"):
                self.insertar()
            elif op == "2":
                self.modificar()
            elif op == "3":
                self.listar()
            elif op == "4":
                self.eliminar()
            elif op == "S" or op == "s":
                print("Salir")
                break
            else:
                op = input("*** Opcion no valida ***")
                            

if __name__ == "__main__":
    app = crud()
    app.muestra_menu()    