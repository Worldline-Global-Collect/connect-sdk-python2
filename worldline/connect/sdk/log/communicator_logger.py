from abc import ABCMeta, abstractmethod


class CommunicatorLogger(object):
    """
    Used to log messages from communicators.
    """
    __metaclass__ = ABCMeta

    def log_request(self, request_log_message):
        """
        Logs a request message object

        """
        self.log(request_log_message.get_message())

    def log_response(self, response_log_message):
        """
        Logs a response message object

        """
        self.log(response_log_message.get_message())

    @abstractmethod
    def log(self, message, thrown=None):
        """
        Logs a throwable with an accompanying message.

        :param message: The message accompanying the throwable.
        :param thrown: The throwable to log.
        """
        raise NotImplementedError
