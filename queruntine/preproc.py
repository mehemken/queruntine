# Preprocessor
import json


class Preprocessor:
    def __init__(self, conn_str, queries):
        self.conn_str = conn_str
        self.queries = queries

    def get_payload(self):
        return b''

    def _jsonify(self):
        values = {
            'connection_string': self.conn_str,
            'queries': self.queries
        }
        return json.dumps(values)

    def _to_bytes(self):
        return b''
