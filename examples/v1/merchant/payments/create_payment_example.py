#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.api_exception import ApiException
from worldline.connect.sdk.v1.declined_payment_exception import DeclinedPaymentException
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.address_personal import AddressPersonal
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.browser_data import BrowserData
from worldline.connect.sdk.v1.domain.card import Card
from worldline.connect.sdk.v1.domain.card_payment_method_specific_input import CardPaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.company_information import CompanyInformation
from worldline.connect.sdk.v1.domain.contact_details import ContactDetails
from worldline.connect.sdk.v1.domain.create_payment_request import CreatePaymentRequest
from worldline.connect.sdk.v1.domain.customer import Customer
from worldline.connect.sdk.v1.domain.customer_device import CustomerDevice
from worldline.connect.sdk.v1.domain.line_item import LineItem
from worldline.connect.sdk.v1.domain.line_item_invoice_data import LineItemInvoiceData
from worldline.connect.sdk.v1.domain.order import Order
from worldline.connect.sdk.v1.domain.order_invoice_data import OrderInvoiceData
from worldline.connect.sdk.v1.domain.order_references import OrderReferences
from worldline.connect.sdk.v1.domain.personal_information import PersonalInformation
from worldline.connect.sdk.v1.domain.personal_name import PersonalName
from worldline.connect.sdk.v1.domain.redirection_data import RedirectionData
from worldline.connect.sdk.v1.domain.shipping import Shipping
from worldline.connect.sdk.v1.domain.shopping_cart import ShoppingCart
from worldline.connect.sdk.v1.domain.three_d_secure import ThreeDSecure


class CreatePaymentExample(object):

    def example(self):
        with self.__get_client() as client:
            card = Card()
            card.card_number = "4567350000427977"
            card.cardholder_name = "Wile E. Coyote"
            card.cvv = "123"
            card.expiry_date = "1299"

            authentication_amount = AmountOfMoney()
            authentication_amount.amount = 2980
            authentication_amount.currency_code = "EUR"

            redirection_data = RedirectionData()
            redirection_data.return_url = "https://hostname.myownwebsite.url"

            three_d_secure = ThreeDSecure()
            three_d_secure.authentication_amount = authentication_amount
            three_d_secure.authentication_flow = "browser"
            three_d_secure.challenge_canvas_size = "600x400"
            three_d_secure.challenge_indicator = "challenge-requested"
            three_d_secure.exemption_request = "none"
            three_d_secure.redirection_data = redirection_data
            three_d_secure.skip_authentication = False

            card_payment_method_specific_input = CardPaymentMethodSpecificInput()
            card_payment_method_specific_input.card = card
            card_payment_method_specific_input.is_recurring = False
            card_payment_method_specific_input.merchant_initiated_reason_indicator = "delayedCharges"
            card_payment_method_specific_input.payment_product_id = 1
            card_payment_method_specific_input.three_d_secure = three_d_secure
            card_payment_method_specific_input.transaction_channel = "ECOMMERCE"

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 2980
            amount_of_money.currency_code = "EUR"

            billing_address = Address()
            billing_address.additional_info = "b"
            billing_address.city = "Monument Valley"
            billing_address.country_code = "US"
            billing_address.house_number = "13"
            billing_address.state = "Utah"
            billing_address.street = "Desertroad"
            billing_address.zip = "84536"

            company_information = CompanyInformation()
            company_information.name = "Acme Labs"
            company_information.vat_number = "1234AB5678CD"

            contact_details = ContactDetails()
            contact_details.email_address = "wile.e.coyote@acmelabs.com"
            contact_details.fax_number = "+1234567891"
            contact_details.phone_number = "+1234567890"

            browser_data = BrowserData()
            browser_data.color_depth = 24
            browser_data.java_enabled = False
            browser_data.screen_height = "1200"
            browser_data.screen_width = "1920"

            device = CustomerDevice()
            device.accept_header = "texthtml,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
            device.browser_data = browser_data
            device.ip_address = "123.123.123.123"
            device.locale = "en-US"
            device.timezone_offset_utc_minutes = "420"
            device.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1 Safari/605.1.15"

            name = PersonalName()
            name.first_name = "Wile"
            name.surname = "Coyote"
            name.surname_prefix = "E."
            name.title = "Mr."

            personal_information = PersonalInformation()
            personal_information.date_of_birth = "19490917"
            personal_information.gender = "male"
            personal_information.name = name

            customer = Customer()
            customer.account_type = "none"
            customer.billing_address = billing_address
            customer.company_information = company_information
            customer.contact_details = contact_details
            customer.device = device
            customer.locale = "en_US"
            customer.merchant_customer_id = "1234"
            customer.personal_information = personal_information

            invoice_data = OrderInvoiceData()
            invoice_data.invoice_date = "20140306191500"
            invoice_data.invoice_number = "000000123"

            references = OrderReferences()
            references.descriptor = "Fast and Furry-ous"
            references.invoice_data = invoice_data
            references.merchant_order_id = 123456
            references.merchant_reference = "AcmeOrder0001"

            shipping_name = PersonalName()
            shipping_name.first_name = "Road"
            shipping_name.surname = "Runner"
            shipping_name.title = "Miss"

            address = AddressPersonal()
            address.additional_info = "Suite II"
            address.city = "Monument Valley"
            address.country_code = "US"
            address.house_number = "1"
            address.name = shipping_name
            address.state = "Utah"
            address.street = "Desertroad"
            address.zip = "84536"

            shipping = Shipping()
            shipping.address = address

            items = []

            item1_amount_of_money = AmountOfMoney()
            item1_amount_of_money.amount = 2500
            item1_amount_of_money.currency_code = "EUR"

            item1_invoice_data = LineItemInvoiceData()
            item1_invoice_data.description = "ACME Super Outfit"
            item1_invoice_data.nr_of_items = "1"
            item1_invoice_data.price_per_item = 2500

            item1 = LineItem()
            item1.amount_of_money = item1_amount_of_money
            item1.invoice_data = item1_invoice_data

            items.append(item1)

            item2_amount_of_money = AmountOfMoney()
            item2_amount_of_money.amount = 480
            item2_amount_of_money.currency_code = "EUR"

            item2_invoice_data = LineItemInvoiceData()
            item2_invoice_data.description = "Aspirin"
            item2_invoice_data.nr_of_items = "12"
            item2_invoice_data.price_per_item = 40

            item2 = LineItem()
            item2.amount_of_money = item2_amount_of_money
            item2.invoice_data = item2_invoice_data

            items.append(item2)

            shopping_cart = ShoppingCart()
            shopping_cart.items = items

            order = Order()
            order.amount_of_money = amount_of_money
            order.customer = customer
            order.references = references
            order.shipping = shipping
            order.shopping_cart = shopping_cart

            body = CreatePaymentRequest()
            body.card_payment_method_specific_input = card_payment_method_specific_input
            body.order = order

            try:
                response = client.v1().merchant("merchantId").payments().create(body)
            except DeclinedPaymentException as e:
                self.handle_declined_payment(e.create_payment_result)
            except ApiException as e:
                self.handle_api_errors(e.errors)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)

    @staticmethod
    def handle_declined_payment(create_payment_result):
        # handle the result here
        pass

    @staticmethod
    def handle_api_errors(errors):
        # handle the errors here
        pass
