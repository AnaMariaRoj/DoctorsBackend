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

def CreateDoctor(doctor_data: dict):
    try:
        doctor = Practitioner(**doctor_data)
        inserted_id = collection.insert_one(json.loads(doctor.json())).inserted_id
        return "success", str(inserted_id)
    except Exception as e:
        return "error", str(e)

def UpdateDoctor(doctor_id: str, updated_data: dict):
    try:
        result = collection.update_one({"_id": ObjectId(doctor_id)}, {"$set": updated_data})
        if result.modified_count > 0:
            return "success", "Doctor updated successfully"
        return "notFound", "Doctor not found"
    except Exception as e:
        return "error", str(e)

def DeleteDoctor(doctor_id: str):
    try:
        result = collection.delete_one({"_id": ObjectId(doctor_id)})
        if result.deleted_count > 0:
            return "success", "Doctor deleted successfully"
        return "notFound", "Doctor not found"
    except Exception as e:
        return "error", str(e)

