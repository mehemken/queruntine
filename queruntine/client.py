import os
import ctypes
from pathlib import Path

class Client:
    def __init__(self):
        self._mtengine_path = self._get_mtengine_path()
        self._response = ''

    def get_response(self, payload):
        """
        Takes the output of Preprocessor and sends it to Rust
        """
        mtengine = ctypes.cdll.LoadLibrary(self._mtengine_path)
        self._response = mtengine.exec_queries(payload)
        if self._response:
            return True
        return False

    def _get_mtengine_path(self):
        this_file = Path(__file__)
        queruntine_root = os.path.abspath(this_file.parent.parent)
        return os.path.join(queruntine_root, 'libmtengine.so')
