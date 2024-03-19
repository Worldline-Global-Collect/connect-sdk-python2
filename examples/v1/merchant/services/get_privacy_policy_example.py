#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.merchant.services.privacypolicy_params import PrivacypolicyParams


class GetPrivacyPolicyExample(object):

    def example(self):
        with self.__get_client() as client:
            query = PrivacypolicyParams()
            query.locale = "en_US"
            query.payment_product_id = 771

            response = client.v1().merchant("merchantId").services().privacypolicy(query)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
