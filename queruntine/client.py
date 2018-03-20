class Client:
    def __init__(self, payload):
        self._payload = payload

    def get_response(self, mtengine_path):
        """
        Takes the output of Preprocessor and sends it to Rust
        """
        return b''
