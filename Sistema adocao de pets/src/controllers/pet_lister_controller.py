from typing import Dict, List
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from .interfaces.pet_lister_controller import PetListerControllerInterface

class PetListerController(PetListerControllerInterface):
   def __init__(self, pets_repository: PetsRepositoryInterface):
      self.__pets_repository = pets_repository
      
   def list_pets(self) -> Dict:
      pets = self.get_pets_in_db()
      return self.format_response(pets)
   
   def get_pets_in_db(self) -> List[PetsTable]:
      pets = self.__pets_repository.list_pets()
      return pets
   
   def format_response(self, pets: List[PetsTable]) -> Dict:
      formatted_pets = []
      for pet in pets:
         formatted_pets.append({
            'id': pet.id,
            'name': pet.name,
         })
         
      return {
         "data": {
            "type": "Pets",
            "count": len(formatted_pets),
            "attributes": formatted_pets
         }
      }
   