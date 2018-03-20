from .preproc import Preprocessor
from .client import Client
from .postproc import Postprocessor
from .printer import Printer

from pathlib import Path
import os

class Runner:
    def __init__(self, connection_string='', queries=[]):
        self.connection_string = connection_string
        self.queries = queries
        self._payload = self._get_payload()
        self._mtengine_path = self._get_mtengine_path()

    def run(self):
        response = Client(self._payload)
        message = Postprocessor(response)
        return Printer(message)

    def _get_payload(self):
        preproc = Preprocessor(
            self.connection_string,
            self.queries
        )
        return preproc.get_payload()

    def _get_mtengine_path(self):
        this_file = Path(__file__)
        queruntine_root = os.path.abspath(this_file.parent.parent)
        return os.path.join(queruntine_root, 'libmtengine.so')
