#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory


class CancelPayoutExample(object):

    def example(self):
        with self.__get_client() as client:
            client.v1().merchant("merchantId").payouts().cancel("payoutId")

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)