import unittest

from tests.integration import init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.v1.merchant.services.convert_amount_params import ConvertAmountParams
from worldline.connect.sdk.v1.merchant.services.services_client import ServicesClient


class SDKProxyTest(unittest.TestCase):
    def test_sdk_proxy(self):
        request = ConvertAmountParams()
        request.amount = 123L
        request.source = "USD"
        request.target = "EUR"

        with init_utils.create_client_with_proxy() as client:
            services = client.v1().merchant(MERCHANT_ID).services()
            services.convert_amount(request)

            self.assertIsInstance(services, ServicesClient)


if __name__ == '__main__':
    unittest.main()
