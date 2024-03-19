#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.merchant.products.get_product_params import GetProductParams


class GetPaymentProductExample(object):

    def example(self):
        with self.__get_client() as client:
            query = GetProductParams()
            query.country_code = "US"
            query.currency_code = "USD"
            query.locale = "en_US"
            query.amount = 1000
            query.is_recurring = True
            query.is_installments = True
            query.force_basic_flow = False
            query.add_hide("fields")

            response = client.v1().merchant("merchantId").products().get(1, query)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
