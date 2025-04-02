from fhir.resources.practitioner import Practitioner
import json

# Ejemplo de uso
if __name__ == "__main__":
    # JSON string correspondiente al artefacto Practitioner de HL7 FHIR
    doctor_json = '''
    {
      "resourceType": "Practitioner",
      "identifier": [
        {
          "system": "http://cedula",
          "value": "1020713756"
        },
        {
          "system": "http://registro-medico",
          "value": "RM123456"
        }
      ],
      "name": [
        {
          "use": "official",
          "text": "Dr. Mario Enrique Duarte",
          "family": "Duarte",
          "given": [
            "Mario",
            "Enrique"
          ]
        }
      ],
      "telecom": [
        {
          "system": "phone",
          "value": "3142279487",
          "use": "work"
        },
        {
          "system": "email",
          "value": "mardugo@gmail.com",
          "use": "work"
        }
      ],
      "gender": "male",
      "address": [
        {
          "use": "work",
          "line": [
            "Cra 55A # 167A - 30"
          ],
          "city": "Bogotá",
          "state": "Cundinamarca",
          "postalCode": "11156",
          "country": "Colombia"
        }
      ],
      "qualification": [
        {
          "identifier": {
            "system": "http://registro-medico",
            "value": "RM123456"
          },
          "code": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/v2-0360/2.7",
                "code": "MD",
                "display": "Medical Doctor"
              }
            ]
          }
        }
      ]
    }
    '''

    doc = Practitioner.model_validate(json.loads(doctor_json))
    print("JSON::", doc.model_dump())
