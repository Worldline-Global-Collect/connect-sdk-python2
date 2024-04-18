#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.api_exception import ApiException
from worldline.connect.sdk.v1.declined_refund_exception import DeclinedRefundException
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.refund_references import RefundReferences
from worldline.connect.sdk.v1.domain.refund_request import RefundRequest


class CreateRefundCaptureExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 500
            amount_of_money.currency_code = 'EUR'

            refund_references = RefundReferences()
            refund_references.merchant_reference = 'AcmeOrder0001'

            body = RefundRequest()
            body.amount_of_money = amount_of_money
            body.refund_references = refund_references

            try:
                response = client.v1().merchant('merchantId').captures().refund('captureId', body)
            except DeclinedRefundException as e:
                self.handle_declined_refund(e.refund_result)
            except ApiException as e:
                self.handle_error_response(e.error_id, e.errors)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)

    @staticmethod
    def handle_declined_refund(refund_result):
        # handle the result here
        pass

    @staticmethod
    def handle_error_response(error_id, errors):
        # handle the error response here
        pass
