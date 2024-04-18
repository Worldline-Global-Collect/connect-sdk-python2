#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.api_exception import ApiException
from worldline.connect.sdk.v1.declined_payout_exception import DeclinedPayoutException
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.bank_account_iban import BankAccountIban
from worldline.connect.sdk.v1.domain.bank_transfer_payout_method_specific_input import BankTransferPayoutMethodSpecificInput
from worldline.connect.sdk.v1.domain.company_information import CompanyInformation
from worldline.connect.sdk.v1.domain.contact_details_base import ContactDetailsBase
from worldline.connect.sdk.v1.domain.create_payout_request import CreatePayoutRequest
from worldline.connect.sdk.v1.domain.payout_customer import PayoutCustomer
from worldline.connect.sdk.v1.domain.payout_details import PayoutDetails
from worldline.connect.sdk.v1.domain.payout_references import PayoutReferences
from worldline.connect.sdk.v1.domain.personal_name import PersonalName


class CreatePayoutExample(object):

    def example(self):
        with self.__get_client() as client:
            bank_account_iban = BankAccountIban()
            bank_account_iban.account_holder_name = 'Wile E. Coyote'
            bank_account_iban.iban = 'IT60X0542811101000000123456'

            bank_transfer_payout_method_specific_input = BankTransferPayoutMethodSpecificInput()
            bank_transfer_payout_method_specific_input.bank_account_iban = bank_account_iban
            bank_transfer_payout_method_specific_input.payout_date = '20150102'
            bank_transfer_payout_method_specific_input.payout_text = 'Payout Acme'
            bank_transfer_payout_method_specific_input.swift_code = 'swift'

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2345
            amount_of_money.currency_code = 'EUR'

            address = Address()
            address.city = 'Burbank'
            address.country_code = 'US'
            address.house_number = '411'
            address.state = 'California'
            address.street = 'N Hollywood Way'
            address.zip = '91505'

            company_information = CompanyInformation()
            company_information.name = 'Acme Labs'

            contact_details = ContactDetailsBase()
            contact_details.email_address = 'wile.e.coyote@acmelabs.com'

            name = PersonalName()
            name.first_name = 'Wile'
            name.surname = 'Coyote'
            name.surname_prefix = 'E.'
            name.title = 'Mr.'

            customer = PayoutCustomer()
            customer.address = address
            customer.company_information = company_information
            customer.contact_details = contact_details
            customer.name = name

            references = PayoutReferences()
            references.merchant_reference = 'AcmeOrder001'

            payout_details = PayoutDetails()
            payout_details.amount_of_money = amount_of_money
            payout_details.customer = customer
            payout_details.references = references

            body = CreatePayoutRequest()
            body.bank_transfer_payout_method_specific_input = bank_transfer_payout_method_specific_input
            body.payout_details = payout_details

            try:
                response = client.v1().merchant('merchantId').payouts().create(body)
            except DeclinedPayoutException as e:
                self.handle_declined_payout(e.payout_result)
            except ApiException as e:
                self.handle_error_response(e.error_id, e.errors)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)

    @staticmethod
    def handle_declined_payout(payout_result):
        # handle the result here
        pass

    @staticmethod
    def handle_error_response(error_id, errors):
        # handle the error response here
        pass
