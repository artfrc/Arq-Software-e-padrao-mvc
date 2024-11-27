from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
   def list_pets(self):
      return [
         PetsTable(name='Rex', type='dog', id=4),
         PetsTable(name='Buddy', type='dog', id=47),
      ]
      
def test_list_pets():
  controller = PetListerController((MockPetsRepository()))
  response = controller.list_pets()
  
  expected_response = {
         "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
               {"id": 4, "name": "Rex"}, 
               { "id": 47,"name": "Buddy"}
            ]
         }
      }
  
  assert response == expected_response