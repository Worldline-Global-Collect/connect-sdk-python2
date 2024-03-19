import unittest
import uuid

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.call_context import CallContext
from worldline.connect.sdk.v1.declined_payment_exception import DeclinedPaymentException
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.create_payment_request import CreatePaymentRequest
from worldline.connect.sdk.v1.domain.customer import Customer
from worldline.connect.sdk.v1.domain.order import Order
from worldline.connect.sdk.v1.domain.redirect_payment_method_specific_input import RedirectPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.redirect_payment_product809_specific_input import RedirectPaymentProduct809SpecificInput


class IdempotenceTest(unittest.TestCase):
    """Test that the client can successfully detect that an idempotent request is sent twice"""
    def test_idempotence(self):
        """Test that the client can successfully detect that an idempotent request is sent twice"""

        amount_of_money = AmountOfMoney()
        amount_of_money.currency_code = "EUR"
        amount_of_money.amount = 100L
        billing_address = Address()
        billing_address.country_code = "NL"
        customer = Customer()
        customer.locale = "en"
        customer.billing_address = billing_address
        order = Order()
        order.amount_of_money = amount_of_money
        order.customer = customer
        payment_product_input = RedirectPaymentProduct809SpecificInput()
        payment_product_input.issuer_id = "INGBNL2A"
        payment_method_input = RedirectPaymentMethodSpecificInput()
        payment_method_input.return_url = "http://example.com"
        payment_method_input.payment_product_id = 809
        payment_method_input.payment_product809_specific_input = payment_product_input
        body = CreatePaymentRequest()
        body.order = order
        body.redirect_payment_method_specific_input = payment_method_input
        idempotence_key = str(uuid.uuid4())
        context = CallContext(idempotence_key)

        with init_utils.create_client() as client:
            def do_create_payment():
                # For this test it doesn't matter if the response is successful or declined,
                # as long as idempotence is handled correctly
                try:
                    return client.v1().merchant(MERCHANT_ID).payments().create(body, context)
                except DeclinedPaymentException as e:
                    return e.create_payment_result

            result = do_create_payment()

            payment_id = result.payment.id
            status = result.payment.status

            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNone(context.idempotence_request_timestamp)

            result_2 = do_create_payment()

            payment_id_2 = result_2.payment.id
            status_2 = result_2.payment.status
            self.assertEqual(payment_id, payment_id_2)
            self.assertEqual(status, status_2)
            self.assertEqual(idempotence_key, context.idempotence_key)
            self.assertIsNotNone(context.idempotence_request_timestamp)


if __name__ == '__main__':
    unittest.main()
