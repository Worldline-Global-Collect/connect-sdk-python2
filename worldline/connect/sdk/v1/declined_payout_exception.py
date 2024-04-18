#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from declined_transaction_exception import DeclinedTransactionException


class DeclinedPayoutException(DeclinedTransactionException):
    """
    Represents an error response from a payout call.
    """

    def __init__(self, status_code, response_body, response):
        if response is not None:
            super(DeclinedPayoutException, self).__init__(status_code, response_body, response.error_id, response.errors,
                                                          DeclinedPayoutException.__create_message(response))
        else:
            super(DeclinedPayoutException, self).__init__(status_code, response_body, None, None,
                                                          DeclinedPayoutException.__create_message(response))
        self.__response = response

    @staticmethod
    def __create_message(response):
        if response is not None:
            payout_result = response.payout_result
        else:
            payout_result = None
        if payout_result is not None:
            return "declined payout '%s' with status '%s'" % (payout_result.id, payout_result.status)
        else:
            return "the Worldline Global Collect platform returned a declined payout response"

    @property
    def payout_result(self):
        """
        :return: The result of creating a payout if available, otherwise None.
        """
        if self.__response is None:
            return None
        else:
            return self.__response.payout_result
