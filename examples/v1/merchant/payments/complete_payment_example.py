#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.card_without_cvv import CardWithoutCvv
from worldline.connect.sdk.v1.domain.complete_payment_card_payment_method_specific_input import CompletePaymentCardPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.complete_payment_request import CompletePaymentRequest


class CompletePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            card = CardWithoutCvv()
            card.card_number = '67030000000000003'
            card.cardholder_name = 'Wile E. Coyote'
            card.expiry_date = '1299'

            card_payment_method_specific_input = CompletePaymentCardPaymentMethodSpecificInput()
            card_payment_method_specific_input.card = card

            body = CompletePaymentRequest()
            body.card_payment_method_specific_input = card_payment_method_specific_input

            response = client.v1().merchant('merchantId').payments().complete('paymentId', body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
