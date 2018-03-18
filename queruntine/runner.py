from .preproc import Preprocessor
from .client import Client
from .postproc import Postprocessor
from .printer import Printer

class Runner:
    def __init__(self, connection_string='', queries=[]):
        self.connection_string = connection_string
        self.queries = queries

    def run(self):
        preproc = Preprocessor(
            self.connection_string,
            self.queries
        )
        payload = preproc.get_payload()
        
        response = Client(payload)
        message = Postprocessor(response)
        return Printer(message)
