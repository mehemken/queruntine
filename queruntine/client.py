class Client:
    def __init__(self, payload):
        self._payload = payload

    def send(self):
        """
        Takes the output of Preprocessor and sends it to Rust
        """
        pass

    def receive(self):
        pass
