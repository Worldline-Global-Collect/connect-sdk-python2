#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.create_dispute_request import CreateDisputeRequest


class CreatePaymentDisputeExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 1234
            amount_of_money.currency_code = 'USD'

            body = CreateDisputeRequest()
            body.amount_of_money = amount_of_money
            body.contact_person = 'Wile Coyote'
            body.email_address = 'wile.e.coyote@acmelabs.com'
            body.reply_to = 'r.runner@acmelabs.com'
            body.request_message = 'This is the message from the merchant to GlobalCollect. It is a a freeform text field.'

            response = client.v1().merchant('merchantId').payments().dispute('paymentId', body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
