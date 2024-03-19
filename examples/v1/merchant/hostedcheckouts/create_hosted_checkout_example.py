#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.create_hosted_checkout_request import CreateHostedCheckoutRequest
from worldline.connect.sdk.v1.domain.customer import Customer
from worldline.connect.sdk.v1.domain.hosted_checkout_specific_input import HostedCheckoutSpecificInput
from worldline.connect.sdk.v1.domain.order import Order


class CreateHostedCheckoutExample(object):

    def example(self):
        with self.__get_client() as client:
            hosted_checkout_specific_input = HostedCheckoutSpecificInput()
            hosted_checkout_specific_input.locale = "en_GB"
            hosted_checkout_specific_input.variant = "testVariant"

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2345
            amount_of_money.currency_code = "USD"

            billing_address = Address()
            billing_address.country_code = "US"

            customer = Customer()
            customer.billing_address = billing_address
            customer.merchant_customer_id = "1234"

            order = Order()
            order.amount_of_money = amount_of_money
            order.customer = customer

            body = CreateHostedCheckoutRequest()
            body.hosted_checkout_specific_input = hosted_checkout_specific_input
            body.order = order

            response = client.v1().merchant("merchantId").hostedcheckouts().create(body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
