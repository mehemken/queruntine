import os
import ctypes

class Client:
    def __init__(self, payload):
        self._payload = payload

    def get_response(self, mtengine_path):
        """
        Takes the output of Preprocessor and sends it to Rust
        """
        mtengine = ctypes.cdll.LoadLibrary(mtengine_path)
        return mtengine.exec_queries(self._payload)
