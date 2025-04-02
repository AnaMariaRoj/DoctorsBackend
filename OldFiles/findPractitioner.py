from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para buscar practitionerses por un identifier específico
def find_practitioner_by_identifier(collection, identifier_type, identifier_value):
    try:
        # Consultar el documento que coincida con el identifier
        query = {
            "identifier": {
                "$elemMatch": {
                    "type": identifier_type,
                    "value": identifier_value
                }
            }
        }
        practitioner = collection.find_one(query)
        
        # Retornar el practitioners encontrado
        return practitioner
    except Exception as e:
        print(f"Error al buscar en MongoDB: {e}")
        return None

# Función para mostrar los datos de un practitioners
def display_practitioner(practitioner):
    if practitioner:
        print("Médico encontrado:")
        print(f"  ID: {practitioner.get('_id')}")
        print(f"  Nombre: {practitioner.get('name', [{}])[0].get('given', [''])[0]} {practitioner.get('name', [{}])[0].get('family', '')}")
        print(f"  Género: {practitioner.get('gender', 'Desconocido')}")
        print(f"  Especialidad: {practitioner.get('specialty', 'No especificada')}")
        print("  Identificadores:")
        for identifier in practitioner.get("identifier", []):
            print(f"    Type: {identifier.get('type')}, Valor: {identifier.get('value')}")
    else:
        print("No se encontró ningún Médico con el identifier especificado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "practitioners"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)
    
    # Identifier específico a buscar (reemplaza con los valores que desees)
    identifier_type = "cc"
    identifier_value = "1020713756"
    
    # Buscar el practitioners por identifier
    practitioner = find_practitioner_by_identifier(collection, identifier_type, identifier_value)
    
    # Mostrar los datos del practitioners encontrado
    display_practitioner(practitioner)
