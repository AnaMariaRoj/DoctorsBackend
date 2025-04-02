import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para leer todos los doctores de la colección
def read_practitioners_from_mongodb(collection):
    try:
        # Consultar todos los documentos en la colección
        practitioners = collection.find()
        
        # Convertir los documentos a una lista de diccionarios
        practitioner_list = list(practitioners)
        
        # Retornar la lista de doctores
        return practitioner_list
    except Exception as e:
        print(f"Error al leer desde MongoDB: {e}")
        return None

# Función para mostrar los datos de los doctores
def display_practitioners(practitioner_list):
    if practitioner_list:
        for practitioner in practitioner_list:
            print("Doctor:")
            print(f"  ID: {practitioner.get('_id')}")
            print(f"  Nombre: {practitioner.get('name', [{}])[0].get('given', [''])[0]} {practitioner.get('name', [{}])[0].get('family', '')}")
            print(f"  Especialidad: {practitioner.get('specialty', 'No especificada')}")
            print(f"  Género: {practitioner                                                                                                                             .get('gender', 'Desconocido')}")
            print("-" * 30)
    else:
        print("No se encontraron doctores en la base de datos.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "practitioners"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Leer los doctores de la colección
    practitioners = read_practitioners_from_mongodb(collection)
    
    # Mostrar los datos de los doctores
    display_practitioners(practitioners)
