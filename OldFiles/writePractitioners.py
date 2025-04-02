import json
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Función para conectar a la base de datos MongoDB
def connect_to_mongodb(uri, db_name, collection_name):
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client[db_name]
    collection = db[collection_name]
    return collection

# Función para guardar en MongoDB
def save_practitioner_to_mongodb(practitioner_json, collection):
    try:
        # Convertir el JSON string a un diccionario de Python
        practitioner_data = json.loads(practitioner_json)

        # Insertar el documento en la colección de MongoDB
        result = collection.insert_one(practitioner_data)

        # Retornar el ID del documento insertado
        return result.inserted_id
    except Exception as e:
        print(f"Error al guardar en MongoDB: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Cadena de conexión a MongoDB (reemplaza con tu propia cadena de conexión)
    uri = "mongodb+srv://mardugo:clave@sampleinformationservic.t2yog.mongodb.net/?retryWrites=true&w=majority&appName=SampleInformationService"

    # Nombre de la base de datos y la colección
    db_name = "HIS"
    collection_name = "practitioners"

    # Conectar a MongoDB
    collection = connect_to_mongodb(uri, db_name, collection_name)

    # JSON string correspondiente al artefacto Practitioner de HL7 FHIR
    practitioner_json = f'''
    {{
      "resourceType": "Practitioner",
      "identifier": [
        {{
          "type": "cc",
          "value": "123456789"
        }},
        {{
          "type": "license",
          "value": "MED12345"
        }}
      ],
      "name": [
        {{
          "use": "official",
          "text": "Dr. Juan Pérez",
          "family": "Pérez",
          "given": [
            "Juan",
            "Carlos"
          ]
        }}
      ],
      "telecom": [
        {{
          "system": "phone",
          "value": "3123456789",
          "use": "work"
        }},
        {{
          "system": "email",
          "value": "juan.perez@hospital.com",
          "use": "work"
        }}
      ],
      "gender": "male",
      "birthDate": "1975-08-20",
      "address": [
        {{
          "use": "work",
          "line": [
            "Av. Siempre Viva 123"
          ],
          "city": "Medellín",
          "state": "Antioquia",
          "postalCode": "050001",
          "country": "Colombia"
        }}
      ],
      "qualification": [
        {{
          "code": "Médico General",
          "issuer": "Universidad Nacional"
        }}
      ]
    }}
    '''

    # Guardar el JSON en MongoDB
    inserted_id = save_practitioner_to_mongodb(practitioner_json, collection)

    if inserted_id:
        print(f"Médico guardado con ID: {inserted_id}")
    else:
        print("No se pudo guardar el médico.")
