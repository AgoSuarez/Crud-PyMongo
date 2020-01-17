from pymongo import MongoClient

class Agenda:
    def __init__(self):
        #creamos una conexion a MongoDB
        con = MongoClient('localhost:27017')
        #Conectamos con nuestra base de datos crudMongoPy
        self.db = con.crudMongoPy

    def insertar(self, id, Nombre, Apellido, Telefono):
        try:
            #Insertamos los datos en nuestra coleccion
            self.db.contactos.insert_one(
            {
                'id': int(id),
                'nombre' : Nombre,
                'apellido' : Apellido,
                'telefono' : Telefono
            })
            print("Datos ha sido añadidos con exito")
        except expression as identifier:
            print(identifier)
        
    def buscar(self, id):
        try:
            print(id)
            id = {'id': int(id)}
            dato = self.db.contactos.find_one(id)
            return dato
        except expression as identifier:
            pass
        print(f"buscar datos {id}")

    def actualizar(self, id, nombre, apellido, telefono):
        id = {'id': int(id)}
        #Localizamos el registro y lo actualizamos
        self.db.contactos.update_one(id, {'$set' : {'nombre' : nombre, 'apellido' : apellido, 'telefono' : telefono}})

    def listar(self):
        try:
            #Buscamos todos los registros y los devolvemos
            reg = self.db.contactos.find()
            return reg
        except expression as identifier:
            print(identifier)
        
    def eliminar(self, id):
        id = {'id': int(id)}
        self.db.contactos.delete_one(id)
        print("Eliminar datos")
