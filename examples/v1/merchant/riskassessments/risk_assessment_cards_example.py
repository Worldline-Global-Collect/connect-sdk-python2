#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
import os

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.v1.domain.additional_order_input_airline_data import AdditionalOrderInputAirlineData
from worldline.connect.sdk.v1.domain.address import Address
from worldline.connect.sdk.v1.domain.airline_data import AirlineData
from worldline.connect.sdk.v1.domain.airline_flight_leg import AirlineFlightLeg
from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.card import Card
from worldline.connect.sdk.v1.domain.customer_risk_assessment import CustomerRiskAssessment
from worldline.connect.sdk.v1.domain.order_risk_assessment import OrderRiskAssessment
from worldline.connect.sdk.v1.domain.risk_assessment_card import RiskAssessmentCard


class RiskAssessmentCardsExample(object):

    def example(self):
        with self.__get_client() as client:
            card = Card()
            card.card_number = "4567350000427977"
            card.cvv = "123"
            card.expiry_date = "1299"

            flight_legs = []

            flight_leg1 = AirlineFlightLeg()
            flight_leg1.airline_class = "1"
            flight_leg1.arrival_airport = "AMS"
            flight_leg1.carrier_code = "KL"
            flight_leg1.date = "20150102"
            flight_leg1.departure_time = "17:59"
            flight_leg1.fare = "fare"
            flight_leg1.fare_basis = "INTERNET"
            flight_leg1.flight_number = "791"
            flight_leg1.number = 1
            flight_leg1.origin_airport = "BCN"
            flight_leg1.stopover_code = "non-permitted"

            flight_legs.append(flight_leg1)

            flight_leg2 = AirlineFlightLeg()
            flight_leg2.airline_class = "1"
            flight_leg2.arrival_airport = "BCN"
            flight_leg2.carrier_code = "KL"
            flight_leg2.date = "20150102"
            flight_leg2.departure_time = "23:59"
            flight_leg2.fare = "fare"
            flight_leg2.fare_basis = "INTERNET"
            flight_leg2.flight_number = "792"
            flight_leg2.number = 2
            flight_leg2.origin_airport = "AMS"
            flight_leg2.stopover_code = "non-permitted"

            flight_legs.append(flight_leg2)

            airline_data = AirlineData()
            airline_data.agent_numeric_code = "123321"
            airline_data.code = "123"
            airline_data.flight_date = "20150102"
            airline_data.flight_legs = flight_legs
            airline_data.invoice_number = "123456"
            airline_data.is_e_ticket = True
            airline_data.is_restricted_ticket = True
            airline_data.is_third_party = True
            airline_data.issue_date = "20150101"
            airline_data.merchant_customer_id = "14"
            airline_data.name = "Air France KLM"
            airline_data.passenger_name = "WECOYOTE"
            airline_data.place_of_issue = "Utah"
            airline_data.pnr = "4JTGKT"
            airline_data.point_of_sale = "IATA point of sale name"
            airline_data.pos_city_code = "AMS"
            airline_data.ticket_delivery_method = "e-ticket"
            airline_data.ticket_number = "KLM20050000"

            additional_input = AdditionalOrderInputAirlineData()
            additional_input.airline_data = airline_data

            amount_of_money = AmountOfMoney()
            amount_of_money.amount = 100
            amount_of_money.currency_code = "EUR"

            billing_address = Address()
            billing_address.country_code = "US"

            customer = CustomerRiskAssessment()
            customer.account_type = "existing"
            customer.billing_address = billing_address
            customer.locale = "en_US"

            order = OrderRiskAssessment()
            order.additional_input = additional_input
            order.amount_of_money = amount_of_money
            order.customer = customer

            body = RiskAssessmentCard()
            body.card = card
            body.order = order

            response = client.v1().merchant("merchantId").riskassessments().cards(body)

    @staticmethod
    def __get_client():
        api_key_id = os.getenv("connect.api.apiKeyId", "someKey")
        secret_api_key = os.getenv("connect.api.secretApiKey", "someSecret")
        configuration_file_name = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                               '../../../example_configuration.ini'))
        return Factory.create_client_from_file(configuration_file_name, api_key_id, secret_api_key)
