import re
from typing import Dict
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
   def __init__(self, people_repository: PeopleRepositoryInterface):
      self.__people_repository = people_repository
      
   def create(self, person_info: Dict) -> Dict:
      first_name = person_info["first_name"]
      last_name = person_info["last_name"]
      age = person_info["age"]
      pet_id = person_info["pet_id"]
      
      self.__validate_first_and_last_name(first_name, last_name)
      self.__validate_age_and_pet_id(age, pet_id)
      self.__insert_person_in_database(first_name, last_name, age, pet_id)
      return self.__format_response(person_info)
      
   def __validate_first_and_last_name(self, first_name: str, last_name: str):
      # Expressão regular para caracteres que não são letras
      non_valid_characters = re.compile(r'[^a-zA-Z\s]')
      if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
         raise HttpBadRequestError("First name or last name contains invalid characters!")
      
   def __validate_age_and_pet_id(self, age: int, pet_id: int):
      # Expressão regular para caracteres que não são números
      non_valid_characters = re.compile(r'[^0-9]')
      
      if non_valid_characters.search(str(age)) or non_valid_characters.search(str(pet_id)):
         raise HttpBadRequestError("People age or pet_id invalid!")
      
   def __insert_person_in_database(self, first_name: str, last_name: str, age: int, pet_id: int):
      self.__people_repository.insert_person(first_name, last_name, age, pet_id)
      
   def __format_response(self, person_info: Dict) -> Dict:
      return {
         "data": {
            "type": "Person",
            "count": 1,
            "attributes": person_info
         }
      }
