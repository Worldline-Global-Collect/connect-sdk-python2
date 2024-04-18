#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.session_request import SessionRequest


class CreateSessionExample(object):

    def example(self):
        with self.__get_client() as client:
            tokens = []
            tokens.append('126166b16ed04b3ab85fb06da1d7a167')
            tokens.append('226166b16ed04b3ab85fb06da1d7a167')
            tokens.append('122c5b4d-dd40-49f0-b7c9-3594212167a9')
            tokens.append('326166b16ed04b3ab85fb06da1d7a167')
            tokens.append('426166b16ed04b3ab85fb06da1d7a167')

            body = SessionRequest()
            body.tokens = tokens

            response = client.v1().merchant('merchantId').sessions().create(body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
