from flask_restful import Resource
from flask import request
from models.medication_list import MedicationList
from models.db import db

class MedicationLists(Resource):
    def get(self):
        data = MedicationList.find_all()
        results = [u.json() for u in data]
        return results
    
    def post(self):
        data = request.get_json()
        medication_list = MedicationList(**data)
        medication_list.create()
        return medication_list.json(), 201