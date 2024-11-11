from services.SymtomService import SymptomService
from dto.Symtom import SymptomDto

class SymptomController:
    def __init__(self):
        self.service = SymptomService()

    def create_symptom(self, symptom_data:SymptomDto):
        return self.service.CreateSymptom(symptom_data)

    def edit_symptom(self, symptom_data:SymptomDto, symptom_id:int):
        return self.service.EditSymptom(symptom_data, symptom_id)

    def search_by_id(self, symptom_id:int):
        return self.service.SearchById(symptom_id)

    def delete_symptom(self, symptom_id:int):
        return self.service.Delete(symptom_id)

    def get_symptoms(self):
        return self.service.GetSymptoms()
