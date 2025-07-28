import unittest

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.v1.domain.amount_of_money import AmountOfMoney
from worldline.connect.sdk.v1.domain.bank_account_bban import BankAccountBban
from worldline.connect.sdk.v1.domain.customer_risk_assessment import CustomerRiskAssessment
from worldline.connect.sdk.v1.domain.order_risk_assessment import OrderRiskAssessment
from worldline.connect.sdk.v1.domain.risk_assessment_bank_account import RiskAssessmentBankAccount


class RiskAssessmentsTest(unittest.TestCase):
    """Test if the risk assessments service functions"""
    def test_risk_assessments(self):
        """Test if the risk assessments service functions"""
        self.skipTest("Risk assessments are not available for pre-prod sandbox accounts")

        bank_account_bban = BankAccountBban()
        bank_account_bban.country_code = "DE"
        bank_account_bban.account_number = "0532013000"
        bank_account_bban.bank_code = "37040044"
        amount_of_money = AmountOfMoney()
        amount_of_money.amount = 100L
        amount_of_money.currency_code = "EUR"
        customer = CustomerRiskAssessment()
        customer.locale = "en_GB"
        order = OrderRiskAssessment()
        order.amount_of_money = amount_of_money
        order.customer = customer
        body = RiskAssessmentBankAccount()
        body.order = order
        body.bank_account_bban = bank_account_bban

        with init_utils.create_client() as client:
            response = client.v1().merchant(MERCHANT_ID).riskassessments().bankaccounts(body)
        self.assertGreater(len(response.results), 0)


if __name__ == '__main__':
    unittest.main()
