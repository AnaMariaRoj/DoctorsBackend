from connection import connect_to_mongodb
from bson import ObjectId
from fhir.resources.practitioner import Practitioner
import json

collection = connect_to_mongodb("HIS", "practitioners")

def GetPractitionersById(practitioners_id: str):
    try:
        practitioners = collection.find_one({"_id": ObjectId(practitioners_id)})
        if practitioners:
            practitioners["_id"] = str(practitioners["_id"])
            return "success", practitioners
        return "notFound", None
    except Exception as e:
        return "notFound", None


def WritePractitioners(practitioners_dict: dict):
    try:
        pat = practitioners.model_validate(practitioners_dict)
    except Exception as e:
        return f"errorValidating: {str(e)}",None
    validated_practitioners_json = pat.model_dump()
    result = collection.insert_one(practitioners_dict)
    if result:
        inserted_id = str(result.inserted_id)
        return "success",inserted_id
    else:
        return "errorInserting", None

