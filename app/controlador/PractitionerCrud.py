from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.practitioner import Practitioner
import json
from pymongo import MongoClient

collection = connect_to_mongodb("HIS", "practitioners")

def GetPractitionerById(practitioner_id: str):
    try:
        practitioner = collection.find_one({"_id": ObjectId(practitioner_id)})
        if practitioner:
            practitioner["_id"] = str(practitioner["_id"])
            return "success", practitioner
        return "notFound", None
    except Exception as e:
        return f"notFound",None

def WritePractitioner(practitioner_dict: dict):
    try:
        pra = Practitioner.model_validate(practitioner_dict)
    except Exception as e:
        print(f"Error de validación: {str(e)}") 
        return f"errorValidating: {str(e)}", None
    validated_practitioner_json = pra.model_dump()
    try:
        result = collection.insert_one(validated_practitioner_json)
        return "success", str(result.inserted_id)
    except Exception as e:
        print(f"Error al insertar en MongoDB: {str(e)}") 
        return "errorInserting", None
