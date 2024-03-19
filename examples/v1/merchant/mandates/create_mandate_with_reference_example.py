#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.bank_account_iban import BankAccountIban
from worldline.connect.sdk.v1.domain.create_mandate_request import CreateMandateRequest
from worldline.connect.sdk.v1.domain.mandate_address import MandateAddress
from worldline.connect.sdk.v1.domain.mandate_contact_details import MandateContactDetails
from worldline.connect.sdk.v1.domain.mandate_customer import MandateCustomer
from worldline.connect.sdk.v1.domain.mandate_personal_information import MandatePersonalInformation
from worldline.connect.sdk.v1.domain.mandate_personal_name import MandatePersonalName


class CreateMandateWithReferenceExample(object):

    def example(self):
        with self.__get_client() as client:
            bank_account_iban = BankAccountIban()
            bank_account_iban.iban = "DE46720200700359736690"

            contact_details = MandateContactDetails()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"

            mandate_address = MandateAddress()
            mandate_address.city = "Monumentenvallei"
            mandate_address.country_code = "NL"
            mandate_address.street = "Woestijnweg"
            mandate_address.zip = "1337XD"

            name = MandatePersonalName()
            name.first_name = "Wile"
            name.surname = "Coyote"

            personal_information = MandatePersonalInformation()
            personal_information.name = name
            personal_information.title = "Miss"

            customer = MandateCustomer()
            customer.bank_account_iban = bank_account_iban
            customer.company_name = "Acme labs"
            customer.contact_details = contact_details
            customer.mandate_address = mandate_address
            customer.personal_information = personal_information

            body = CreateMandateRequest()
            body.customer = customer
            body.customer_reference = "idonthaveareference"
            body.language = "nl"
            body.recurrence_type = "UNIQUE"
            body.signature_type = "UNSIGNED"

            response = client.v1().merchant("merchantId").mandates().create_with_mandate_reference("42268d8067df43e18a50a2ebf4bdb729", body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
