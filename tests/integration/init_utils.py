import os
from ConfigParser import ConfigParser

from worldline.connect.sdk.communicator import Communicator
from worldline.connect.sdk.communicator_configuration import CommunicatorConfiguration
from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.authentication.v1hmac_authenticator import V1HMACAuthenticator
from worldline.connect.sdk.communication.default_connection import DefaultConnection
from worldline.connect.sdk.communication.metadata_provider import MetadataProvider
from worldline.connect.sdk.json.default_marshaller import DefaultMarshaller

"""File containing a number of creation methods for integration tests"""

PROPERTIES_URL = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.ini"))
PROPERTIES_URL_PROXY = os.path.abspath(os.path.join(__file__, os.pardir, "../resources/configuration.proxy.ini"))
# API_KEY_ID, SECRET_API_KEY and MERCHANT_ID are stored in OS and should be retrieved
API_KEY_ID = os.getenv("connect.api.apiKeyId")
SECRET_API_KEY = os.getenv("connect.api.secretApiKey")
MERCHANT_ID = str(os.getenv("connect.api.merchantId"))
if API_KEY_ID is None:
    raise EnvironmentError("could not access environment variable connect.api.apiKeyId required for testing")
if SECRET_API_KEY is None:
    raise EnvironmentError("could not access environment variable connect.api.secretApiKey required for testing")
if MERCHANT_ID == 'None':
    raise EnvironmentError("could not access environment variable connect.api.merchantId required for testing")


def create_communicator_configuration(properties_url=PROPERTIES_URL, max_connections=None):
    """Convenience method to create a communicator configuration that connects to a host stored in system variables"""
    try:
        parser = ConfigParser()
        parser.read(properties_url)
        with open(properties_url) as f:
            parser.readfp(f)
        configuration = CommunicatorConfiguration(parser, api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY,
                                                  max_connections=max_connections)
    except IOError as e:
        raise RuntimeError("Unable to read configuration", e)
    host = os.getenv("connect.api.endpoint.host")
    if host is not None:
        scheme = os.getenv("connect.api.endpoint.scheme", "https")
        port = int(os.getenv("connect.api.endpoint.port", -1))
        configuration.api_endpoint = "{2}://{0}:{1}".format(host, port, scheme)
    return configuration


def create_communicator():
    host = os.getenv("connect.api.endpoint.host")
    scheme = os.getenv("connect.api.endpoint.scheme", "https")
    port = int(os.getenv("connect.api.endpoint.port", -1))
    if not host:
        raise RuntimeError("unable to read environment variables to find api_endpoint")
    api_endpoint = "{2}://{0}:{1}".format(host, port, scheme)
    authenticator = V1HMACAuthenticator(api_key_id=API_KEY_ID, secret_api_key=SECRET_API_KEY)
    return Communicator(api_endpoint=api_endpoint, authenticator=authenticator,
                        connection=DefaultConnection(3, 3), metadata_provider=MetadataProvider("Worldline"),
                        marshaller=DefaultMarshaller.instance())


def create_client(max_connections=None):
    configuration = create_communicator_configuration(max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration).with_client_meta_info('{"test":"test"}')


def create_client_with_proxy(max_connections=None):
    configuration = create_communicator_configuration(PROPERTIES_URL_PROXY, max_connections=max_connections)
    return Factory.create_client_from_configuration(configuration).with_client_meta_info('{"test":"test"}')
