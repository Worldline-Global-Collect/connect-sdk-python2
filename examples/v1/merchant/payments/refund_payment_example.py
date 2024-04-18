#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.api_exception import ApiException
from worldline.connect.sdk.v1.declined_refund_exception import DeclinedRefundException
from worldline.connect.sdk.v1.domain.address_personal import AddressPersonal
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.bank_account_iban import BankAccountIban
from worldline.connect.sdk.v1.domain.bank_refund_method_specific_input import BankRefundMethodSpecificInput
from worldline.connect.sdk.v1.domain.contact_details_base import ContactDetailsBase
from worldline.connect.sdk.v1.domain.personal_name import PersonalName
from worldline.connect.sdk.v1.domain.refund_customer import RefundCustomer
from worldline.connect.sdk.v1.domain.refund_references import RefundReferences
from worldline.connect.sdk.v1.domain.refund_request import RefundRequest


class RefundPaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 1
            amount_of_money.currency_code = 'EUR'

            bank_account_iban = BankAccountIban()
            bank_account_iban.iban = 'NL53INGB0000000036'

            bank_refund_method_specific_input = BankRefundMethodSpecificInput()
            bank_refund_method_specific_input.bank_account_iban = bank_account_iban

            name = PersonalName()
            name.surname = 'Coyote'

            address = AddressPersonal()
            address.country_code = 'US'
            address.name = name

            contact_details = ContactDetailsBase()
            contact_details.email_address = 'wile.e.coyote@acmelabs.com'
            contact_details.email_message_type = 'html'

            customer = RefundCustomer()
            customer.address = address
            customer.contact_details = contact_details

            refund_references = RefundReferences()
            refund_references.merchant_reference = 'AcmeOrder0001'

            body = RefundRequest()
            body.amount_of_money = amount_of_money
            body.bank_refund_method_specific_input = bank_refund_method_specific_input
            body.customer = customer
            body.refund_date = '20140306'
            body.refund_references = refund_references

            try:
                response = client.v1().merchant('merchantId').payments().refund('paymentId', body)
            except DeclinedRefundException as e:
                self.handle_declined_refund(e.refund_result)
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
    def handle_declined_refund(refund_result):
        # handle the result here
        pass

    @staticmethod
    def handle_error_response(error_id, errors):
        # handle the error response here
        pass
