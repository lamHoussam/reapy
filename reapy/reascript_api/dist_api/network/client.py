from . import _PORT, call_requests

import socket

class Client(socket.socket):

    def __init__(self):
        super(Client, self).__init__()
        self._buffer_size = 4096
        self.connect()

    def connect(self):
        super(Client, self).connect(("localhost", _PORT))
        self.address = self.recv(self._buffer_size).decode("ascii")
        self.is_connected = True
        
    def disconnect(self):
        self.send_request("SERVER.disconnect", (self.address,))
        self.is_connected = False
    
    def get_result(self):
        if not self.is_connected:
            raise DisconnectedError
        result = self.recv(self._buffer_size)
        return call_requests.decode_result(result)
    
    def send_request(self, function_name, args=()):
        if not self.is_connected:
            raise DisconnectedError
        request = call_requests.encode_request(function_name, args)
        self.send(request)


class DisconnectedError(Exception):

    def __init__(self):
        message = "Client disonnected. Call self.connect to reconnect."
        super(DisconnectedError, self).__init__(message)