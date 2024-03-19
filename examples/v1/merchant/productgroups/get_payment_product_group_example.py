#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.merchant.productgroups.get_productgroup_params import GetProductgroupParams


class GetPaymentProductGroupExample(object):

    def example(self):
        with self.__get_client() as client:
            query = GetProductgroupParams()
            query.country_code = "US"
            query.currency_code = "USD"
            query.locale = "en_US"
            query.amount = 1000
            query.is_recurring = True
            query.is_installments = True
            query.add_hide("fields")

            response = client.v1().merchant("merchantId").productgroups().get("cards", query)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
