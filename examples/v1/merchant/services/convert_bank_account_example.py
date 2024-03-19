#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.bank_account_bban import BankAccountBban
from worldline.connect.sdk.v1.domain.bank_details_request import BankDetailsRequest


class ConvertBankAccountExample(object):

    def example(self):
        with self.__get_client() as client:
            bank_account_bban = BankAccountBban()
            bank_account_bban.account_number = "0532013000"
            bank_account_bban.bank_code = "37040044"
            bank_account_bban.country_code = "DE"

            body = BankDetailsRequest()
            body.bank_account_bban = bank_account_bban

            response = client.v1().merchant("merchantId").services().bankaccount(body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
