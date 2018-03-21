# Preprocessor
import json


class Preprocessor:
    """
    The class accepts two arguments and stores them.
    The _jsonify() method turns them into valid json.
    The _to_bytes() method turns them into bytes.
    The user API method, get_payload(), essentially takes
    two strings and returns them as JSON as a byte string.
    """
    def __init__(self, conn_str, queries):
        self.conn_str = conn_str
        self.queries = queries

    def get_payload(self):
        return self._to_bytes()

    def _jsonify(self):
        values = {
            'connection_string': self.conn_str,
            'queries': self.queries
        }
        return json.dumps(values)

    def _to_bytes(self):
        return bytes(self._jsonify(), 'utf-8')
