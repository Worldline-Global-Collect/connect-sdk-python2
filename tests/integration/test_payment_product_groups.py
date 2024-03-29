import unittest

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.v1.merchant.productgroups.get_productgroup_params import GetProductgroupParams


class PaymentProductGroupsTest(unittest.TestCase):
    """Test if product groups function"""
    def test_payment_product_groups(self):
        """Test if product groups function"""
        params = GetProductgroupParams()
        params.country_code = "NL"
        params.currency_code = "EUR"

        with init_utils.create_client() as client:
            response = client.v1().merchant(MERCHANT_ID).productgroups().get("cards", params)
        self.assertEqual("cards", response.id)


if __name__ == '__main__':
    unittest.main()
