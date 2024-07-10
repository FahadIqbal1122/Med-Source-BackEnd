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
        product_ids = data.get('product_ids', [])
        user_id = data.get('user_id')
        medication_list = MedicationList(user_id, product_ids)
        medication_list.create()
        return medication_list.json(), 201
    
class SingleMedicationList(Resource):
    def get(self, id):
        data = MedicationList.find_by_id(id)
        return data.json()
    
    def delete(self, id):
        data = MedicationList.delete_by_id(id)
        return data
    
    def put(self, id):
        updated = MedicationList.update_medication_list(id)
        return updated
    
class DelSingleMedicationList(Resource):
    def put(self, user_id, product_id):
        remove = MedicationList.remove_from_medication_list(user_id,product_id)
        return remove