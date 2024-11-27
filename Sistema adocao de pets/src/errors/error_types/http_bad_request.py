class HttpBadRequestError(Exception):
   def __init__(self, message: str):
       super().__init__(message)
       self.message = message
       self.status_code = 400
       self.name = 'Bad Request'
      