import SocketServer
import contextlib
import thread
from BaseHTTPServer import BaseHTTPRequestHandler

from worldline.connect.sdk.communicator import Communicator
from worldline.connect.sdk.communicator_configuration import CommunicatorConfiguration
from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.authentication.v1hmac_authenticator import V1HMACAuthenticator
from worldline.connect.sdk.communication.default_connection import DefaultConnection
from worldline.connect.sdk.communication.metadata_provider import MetadataProvider
from worldline.connect.sdk.json.default_marshaller import DefaultMarshaller


def create_handler(call_able):
    """Creates a handler that serves requests by calling the callable object
    with this handler as argument
    """
    class RequestHandler(BaseHTTPRequestHandler):

        def do_GET(self):
            call_able(self)

        def do_POST(self):
            call_able(self)

        def do_HEAD(self):
            pass

        def do_DELETE(self):
            call_able(self)
    return RequestHandler


@contextlib.contextmanager
def create_server_listening(call_able):
    """Context manager that creates a thread with a server at localhost which listens for requests
    and responds by calling the *call_able* function.

    :param call_able: a callable function to handle incoming requests, when a request comes in
    the function will be called with a SimpleHTTPRequestHandler to handle the request
    :return the url where the server is listening (http://localhost:port)
    """
    server = SocketServer.TCPServer(('localhost', 0), create_handler(call_able), bind_and_activate=True)
    try:
        # frequent polling server for a faster server shutdown and faster tests
        thread.start_new(server.serve_forever, (0.1,))
        yield 'http://localhost:'+str(server.server_address[1])
    finally:
        server.shutdown()
        server.server_close()


def create_client(httphost, connect_timeout=0.500, socket_timeout=0.500,
                  max_connections=CommunicatorConfiguration.DEFAULT_MAX_CONNECTIONS):
    connection = DefaultConnection(connect_timeout, socket_timeout, max_connections)
    authenticator = V1HMACAuthenticator("apiKey", "secret")
    metadata_provider = MetadataProvider("Worldline")
    communicator = Communicator(httphost, connection, authenticator, metadata_provider, DefaultMarshaller.instance())
    return Factory.create_client_from_communicator(communicator)
