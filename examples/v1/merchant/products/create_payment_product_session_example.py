#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.create_payment_product_session_request import CreatePaymentProductSessionRequest
from worldline.connect.sdk.v1.domain.mobile_payment_product_session302_specific_input import MobilePaymentProductSession302SpecificInput


class CreatePaymentProductSessionExample(object):

    def example(self):
        with self.__get_client() as client:
            payment_product_session302_specific_input = MobilePaymentProductSession302SpecificInput()
            payment_product_session302_specific_input.display_name = 'Worldline'
            payment_product_session302_specific_input.domain_name = 'pay1.checkout.worldline-solutions.com'
            payment_product_session302_specific_input.validation_url = '<VALIDATION URL RECEIVED FROM APPLE>'

            body = CreatePaymentProductSessionRequest()
            body.payment_product_session302_specific_input = payment_product_session302_specific_input

            response = client.v1().merchant('merchantId').products().sessions(302, body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
