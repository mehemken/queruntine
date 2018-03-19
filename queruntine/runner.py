from .preproc import Preprocessor
from .client import Client
from .postproc import Postprocessor
from .printer import Printer

class Runner:
    def __init__(self, connection_string='', queries=[]):
        self.connection_string = connection_string
        self.queries = queries
        self._payload = self._get_payload()

    def run(self):
        response = Client(payload)  # This is a bug...
        message = Postprocessor(response)
        return Printer(message)

    def _get_payload(self):
        preproc = Preprocessor(
            self.connection_string,
            self.queries
        )
        return preproc.get_payload()
