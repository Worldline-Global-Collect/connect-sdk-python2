#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.merchant.services.convert_amount_params import ConvertAmountParams


class ConvertAmountExample(object):

    def example(self):
        with self.__get_client() as client:
            query = ConvertAmountParams()
            query.source = 'EUR'
            query.target = 'USD'
            query.amount = 100

            response = client.v1().merchant('merchantId').services().convert_amount(query)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
