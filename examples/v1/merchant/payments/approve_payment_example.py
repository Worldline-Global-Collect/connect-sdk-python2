#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.approve_payment_non_sepa_direct_debit_payment_method_specific_input import ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.approve_payment_request import ApprovePaymentRequest
from worldline.connect.sdk.v1.domain.order_approve_payment import OrderApprovePayment
from worldline.connect.sdk.v1.domain.order_references_approve_payment import OrderReferencesApprovePayment


class ApprovePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            direct_debit_payment_method_specific_input = ApprovePaymentNonSepaDirectDebitPaymentMethodSpecificInput()
            direct_debit_payment_method_specific_input.date_collect = '20150201'
            direct_debit_payment_method_specific_input.token = 'bfa8a7e4-4530-455a-858d-204ba2afb77e'

            references = OrderReferencesApprovePayment()
            references.merchant_reference = 'AcmeOrder0001'

            order = OrderApprovePayment()
            order.references = references

            body = ApprovePaymentRequest()
            body.amount = 2980
            body.direct_debit_payment_method_specific_input = direct_debit_payment_method_specific_input
            body.order = order

            response = client.v1().merchant('merchantId').payments().approve('paymentId', body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
