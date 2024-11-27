from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.validators.person_creator_validator import person_creator_validator
from .interfaces.view_interface import ViewInterface

class PersonCreatorView(ViewInterface):
   
   def __init__(self, controller: PersonCreatorControllerInterface):
       self.__controller = controller
   
   def handle(self, http_request: HttpRequest) -> HttpResponse:  # pylint: disable=W0237
        person_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)
        
        return HttpResponse(body=body_response, status_code=201)

