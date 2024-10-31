from ConfigParser import NoOptionError
from urlparse import urlparse

from proxy_configuration import ProxyConfiguration

from worldline.connect.sdk.authentication.authorization_type import AuthorizationType
from worldline.connect.sdk.domain.shopping_cart_extension import ShoppingCartExtension


# pylint: disable=too-many-instance-attributes
# Necessary to load information from config
class CommunicatorConfiguration(object):
    """
    Configuration for the communicator.
    """
    # The default number of maximum connections.
    DEFAULT_MAX_CONNECTIONS = 10

    __api_endpoint = None
    __connect_timeout = None
    __socket_timeout = None
    __max_connections = None
    __authorization_type = None
    __authorization_id = None
    __authorization_secret = None
    __proxy_configuration = None
    __integrator = None
    __shopping_cart_extension = None

    def __init__(self, properties=None,
                 api_endpoint=None,
                 authorization_id=None, authorization_secret=None,
                 api_key_id=None, secret_api_key=None,
                 authorization_type=None,
                 connect_timeout=None, socket_timeout=None,
                 max_connections=None, proxy_configuration=None,
                 integrator=None, shopping_cart_extension=None):
        """
        :param properties: a ConfigParser.ConfigParser object containing configuration data
        :param connect_timeout: connection timeout for the network communication in seconds
        :param socket_timeout: socket timeout for the network communication in seconds
        :param max_connections: The maximum number of connections in the connection pool
        """
        if properties and properties.sections() and properties.options("ConnectSDK"):
            self.__api_endpoint = self.__get_endpoint(properties)
            authorization = properties.get("ConnectSDK", "connect.api.authorizationType")
            self.__authorization_type = AuthorizationType.get_authorization(authorization)
            self.__connect_timeout = int(properties.get("ConnectSDK", "connect.api.connectTimeout"))
            self.__socket_timeout = int(properties.get("ConnectSDK", "connect.api.socketTimeout"))
            self.__max_connections = self.__get_property(properties, "connect.api.maxConnections",
                                                         self.DEFAULT_MAX_CONNECTIONS)
            try:
                proxy_uri = properties.get("ConnectSDK", "connect.api.proxy.uri")
            except NoOptionError:
                proxy_uri = None
            try:
                proxy_user = properties.get("ConnectSDK", "connect.api.proxy.username")
            except NoOptionError:
                proxy_user = None
            try:
                proxy_pass = properties.get("ConnectSDK", "connect.api.proxy.password")
            except NoOptionError:
                proxy_pass = None
            if proxy_uri is not None:
                self.__proxy_configuration = ProxyConfiguration.from_uri(proxy_uri, proxy_user, proxy_pass)
            else:
                self.__proxy_configuration = None
            try:
                self.__integrator = properties.get("ConnectSDK", "connect.api.integrator")
            except NoOptionError:
                self.__integrator = None
            try:
                self.__shopping_cart_extension = self.__get_shopping_cart_extension(properties)
            except NoOptionError:
                self.__shopping_cart_extension = None

        if api_endpoint:
            self.api_endpoint = api_endpoint
        if authorization_id:
            self.authorization_id = authorization_id
        if authorization_secret:
            self.authorization_secret = authorization_secret
        if api_key_id:
            self.api_key_id = api_key_id
        if secret_api_key:
            self.secret_api_key = secret_api_key
        if authorization_type:
            self.authorization_type = authorization_type
        if connect_timeout:
            self.connect_timeout = connect_timeout
        if socket_timeout:
            self.socket_timeout = socket_timeout
        if max_connections:
            self.max_connections = max_connections
        if proxy_configuration:
            self.proxy_configuration = proxy_configuration
        if integrator:
            self.integrator = integrator
        if shopping_cart_extension:
            self.shopping_cart_extension = shopping_cart_extension

    @staticmethod
    def __get_property(properties, key, default_value):
        try:
            property_value = properties.get("ConnectSDK", key)
        except NoOptionError:
            property_value = None
        if property_value is not None:
            return int(property_value)
        else:
            return default_value

    def __get_endpoint(self, properties):
        host = properties.get("ConnectSDK", "connect.api.endpoint.host")
        try:
            scheme = properties.get("ConnectSDK", "connect.api.endpoint.scheme")
        except NoOptionError:
            scheme = None
        try:
            port = properties.get("ConnectSDK", "connect.api.endpoint.port")
        except NoOptionError:
            port = None
        if scheme:
            if port:
                return self.__create_uri(scheme, host, int(port))
            else:
                return self.__create_uri(scheme, host, -1)
        elif port:
            return self.__create_uri("https", host, int(port))
        else:
            return self.__create_uri("https", host, -1)

    @staticmethod
    def __create_uri(scheme, host, port):
        if port != -1:
            uri = scheme + "://" + host + ":" + str(port)
        else:
            uri = scheme + "://" + host
        url = urlparse(uri)
        if url.scheme.lower() not in ["http", "https"] or not url.netloc:
            raise ValueError("Unable to construct endpoint URI")
        return url

    @staticmethod
    def __get_shopping_cart_extension(properties):
        try:
            creator = properties.get("ConnectSDK", "connect.api.shoppingCartExtension.creator")
        except NoOptionError:
            creator = None
        try:
            name = properties.get("ConnectSDK", "connect.api.shoppingCartExtension.name")
        except NoOptionError:
            name = None
        try:
            version = properties.get("ConnectSDK", "connect.api.shoppingCartExtension.version")
        except NoOptionError:
            version = None
        try:
            extension_id = properties.get("ConnectSDK", "connect.api.shoppingCartExtension.extensionId")
        except NoOptionError:
            extension_id = None
        if creator is None and name is None and version is None and extension_id is None:
            return None
        else:
            return ShoppingCartExtension(creator, name, version, extension_id)

    @property
    def api_endpoint(self):
        """
        The Worldline Global Collect platform API endpoint URI.
        """
        return self.__api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        if isinstance(api_endpoint, basestring):
            api_endpoint = urlparse(str(api_endpoint))
        if api_endpoint is not None and api_endpoint.path:
            raise ValueError("apiEndpoint should not contain a path")
        if api_endpoint is not None and \
                (api_endpoint.username is not None or api_endpoint.query or api_endpoint.fragment):
            raise ValueError("apiEndpoint should not contain user info, query or fragment")
        self.__api_endpoint = api_endpoint

    @property
    def authorization_id(self):
        """
        An id used for authorization. The meaning of this id is different for each authorization type.
        For instance, for v1HMAC this is the identifier for the secret API key.
        """
        return self.__authorization_id

    @authorization_id.setter
    def authorization_id(self, authorization_id):
        self.__authorization_id = authorization_id

    @property
    def authorization_secret(self):
        """
        A secret used for authorization. The meaning of this secret is different for each authorization type.
        For instance, for v1HMAC this is the secret API key.
        """
        return self.__authorization_secret

    @authorization_secret.setter
    def authorization_secret(self, authorization_secret):
        self.__authorization_secret = authorization_secret

    @property
    def api_key_id(self):
        """
        An identifier for the secret API key. The api_key_id can be
        retrieved from the Configuration Center. This identifier is visible in
        the HTTP request and is also used to identify the correct account.

        This property is an alias for authorization_id
        """
        return self.authorization_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        self.authorization_id = api_key_id

    @property
    def secret_api_key(self):
        """
        A shared secret. The shared secret can be retrieved from the
        Configuration Center. An api_key_id and secret_api_key always go
        hand-in-hand, the difference is that secret_api_key is never visible in
        the HTTP request. This secret is used as input for the HMAC algorithm.

        This property is an alias for authorization_secret
        """
        return self.authorization_secret

    @secret_api_key.setter
    def secret_api_key(self, secret_api_key):
        self.authorization_secret = secret_api_key

    @property
    def authorization_type(self):
        return self.__authorization_type

    @authorization_type.setter
    def authorization_type(self, authorization_type):
        self.__authorization_type = authorization_type

    @property
    def connect_timeout(self):
        """Connection timeout for the underlying network communication in seconds"""
        return self.__connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        self.__connect_timeout = connect_timeout

    @property
    def socket_timeout(self):
        """Socket timeout for the underlying network communication in seconds"""
        return self.__socket_timeout

    @socket_timeout.setter
    def socket_timeout(self, socket_timeout):
        self.__socket_timeout = socket_timeout

    @property
    def max_connections(self):
        return self.__max_connections

    @max_connections.setter
    def max_connections(self, max_connections):
        self.__max_connections = max_connections

    @property
    def proxy_configuration(self):
        return self.__proxy_configuration

    @proxy_configuration.setter
    def proxy_configuration(self, proxy_configuration):
        self.__proxy_configuration = proxy_configuration

    @property
    def integrator(self):
        return self.__integrator

    @integrator.setter
    def integrator(self, integrator):
        self.__integrator = integrator

    @property
    def shopping_cart_extension(self):
        return self.__shopping_cart_extension

    @shopping_cart_extension.setter
    def shopping_cart_extension(self, shopping_cart_extension):
        self.__shopping_cart_extension = shopping_cart_extension
