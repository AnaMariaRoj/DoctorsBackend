from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.practitioner import Practitioner
import json
from pymongo import MongoClient

collection = connect_to_mongodb("HIS", "practitioners")

def GetPractitionersById(practitioners_id: str):
    try:
        practitioners = collection.find_one({"_id": ObjectId(practitioners_id)})
        if practitioners:
            practitioners["_id"] = str(practitioners["_id"])
            return "success", practitioners
        return "notFound", None
    except Exception as e:
        print(f"❌ Error al obtener Practitioner: {e}")
        return "notFound", None

def WritePractitioners(practitioners_dict: dict):
    try:
        pat = Practitioner.model_validate(practitioners_dict)  # ✅ Corrección del nombre
    except Exception as e:
        print(f"❌ Error validando Practitioner: {e}")
        return f"errorValidating: {str(e)}", None
    
    validated_practitioners_json = pat.model_dump()

    try:
        result = collection.insert_one(validated_practitioners_json)  # ✅ Insertamos el objeto validado
        if result.acknowledged:
            inserted_id = str(result.inserted_id)
            print(f"✅ Insertado con éxito. ID: {inserted_id}")
            return "success", inserted_id
        else:
            print("❌ Error: MongoDB no insertó el documento")
            return "errorInserting", None
    except Exception as e:
        print(f"❌ Error al insertar en MongoDB: {e}")
        return "errorInserting", None

def connect_to_mongodb(db_name, collection_name):
    try:
        client = MongoClient("mongodb+srv://usuario:contraseña@cluster.mongodb.net")
        db = client[db_name]
        collection = db[collection_name]
        print("✅ Conexión exitosa a MongoDB")
        return collection
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")
        return None

