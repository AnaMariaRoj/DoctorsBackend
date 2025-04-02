from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.practitioner import Practitioner
import json

collection = connect_to_mongodb("HIS", "practitioners")

def GetDoctorById(doctor_id: str):
    try:
        doctor = collection.find_one({"_id": ObjectId(doctor_id)})
        if doctor:
            doctor["_id"] = str(doctor["_id"])
            return "success", doctor
        return "notFound", None
    except Exception as e:
        return "notFound", None


def WriteDoctor(doctor_dict: dict):
    try:
        pat = Doctor.model_validate(doctor_dict)
    except Exception as e:
        return f"errorValidating: {str(e)}",None
    validated_doctor_json = pat.model_dump()
    result = collection.insert_one(docotr_dict)
    if result:
        inserted_id = str(result.inserted_id)
        return "success",inserted_id
    else:
        return "errorInserting", None

