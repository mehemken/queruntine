# Preprocessor
import json


class Preprocessor:
    def __init__(self, conn_str, queries):
        self.conn_str = conn_str

    def get_payload(self):
        return b''

    def _jsonify(self):
        return self.conn_str

    def _to_bytes(self):
        return b''
