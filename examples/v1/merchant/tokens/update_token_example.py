#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.card_without_cvv import CardWithoutCvv
from worldline.connect.sdk.v1.domain.company_information import CompanyInformation
from worldline.connect.sdk.v1.domain.customer_token import CustomerToken
from worldline.connect.sdk.v1.domain.personal_information_token import PersonalInformationToken
from worldline.connect.sdk.v1.domain.personal_name_token import PersonalNameToken
from worldline.connect.sdk.v1.domain.token_card import TokenCard
from worldline.connect.sdk.v1.domain.token_card_data import TokenCardData
from worldline.connect.sdk.v1.domain.update_token_request import UpdateTokenRequest


class UpdateTokenExample(object):

    def example(self):
        with self.__get_client() as client:
            billing_address = Address()
            billing_address.additional_info = 'b'
            billing_address.city = 'Monument Valley'
            billing_address.country_code = 'US'
            billing_address.house_number = '13'
            billing_address.state = 'Utah'
            billing_address.street = 'Desertroad'
            billing_address.zip = '84536'

            company_information = CompanyInformation()
            company_information.name = 'Acme Labs'

            name = PersonalNameToken()
            name.first_name = 'Wile'
            name.surname = 'Coyote'
            name.surname_prefix = 'E.'

            personal_information = PersonalInformationToken()
            personal_information.name = name

            customer = CustomerToken()
            customer.billing_address = billing_address
            customer.company_information = company_information
            customer.merchant_customer_id = '1234'
            customer.personal_information = personal_information

            card_without_cvv = CardWithoutCvv()
            card_without_cvv.card_number = '4567350000427977'
            card_without_cvv.cardholder_name = 'Wile E. Coyote'
            card_without_cvv.expiry_date = '1299'
            card_without_cvv.issue_number = '12'

            data = TokenCardData()
            data.card_without_cvv = card_without_cvv

            card = TokenCard()
            card.customer = customer
            card.data = data

            body = UpdateTokenRequest()
            body.card = card
            body.payment_product_id = 1

            client.v1().merchant('merchantId').tokens().update('tokenId', body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
