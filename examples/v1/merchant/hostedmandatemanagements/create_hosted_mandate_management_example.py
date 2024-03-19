#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.create_hosted_mandate_management_request import CreateHostedMandateManagementRequest
from worldline.connect.sdk.v1.domain.hosted_mandate_info import HostedMandateInfo
from worldline.connect.sdk.v1.domain.hosted_mandate_management_specific_input import HostedMandateManagementSpecificInput


class CreateHostedMandateManagementExample(object):

    def example(self):
        with self.__get_client() as client:
            create_mandate_info = HostedMandateInfo()
            create_mandate_info.customer_reference = "idonthaveareference"
            create_mandate_info.recurrence_type = "RECURRING"
            create_mandate_info.signature_type = "UNSIGNED"

            hosted_mandate_management_specific_input = HostedMandateManagementSpecificInput()
            hosted_mandate_management_specific_input.locale = "fr_FR"
            hosted_mandate_management_specific_input.return_url = "http://www.example.com"
            hosted_mandate_management_specific_input.variant = "101"

            body = CreateHostedMandateManagementRequest()
            body.create_mandate_info = create_mandate_info
            body.hosted_mandate_management_specific_input = hosted_mandate_management_specific_input

            response = client.v1().merchant("merchantId").hostedmandatemanagements().create(body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
