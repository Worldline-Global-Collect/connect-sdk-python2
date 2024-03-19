import unittest

import tests.integration.init_utils as init_utils
from tests.integration.init_utils import MERCHANT_ID

from worldline.connect.sdk.factory import Factory
from worldline.connect.sdk.communication.metadata_provider import MetadataProvider
from worldline.connect.sdk.communication.request_header import RequestHeader
from worldline.connect.sdk.v1.merchant.products.directory_params import DirectoryParams


class MultiLineHeaderTest(unittest.TestCase):
    """Test if the products service can function with a multiline header"""
    def test_multiline_header(self):
        """Test if the products service can function with a multiline header"""
        multi_line_header = " some value  \r\n \n with        a liberal amount     of \r\n  spaces    "
        configuration = init_utils.create_communicator_configuration()
        metadata_provider = MetadataProvider(integrator="Worldline",
                                             additional_request_headers=(RequestHeader("X-GCS-MultiLineHeader", multi_line_header), ))
        params = DirectoryParams()
        params.country_code = "NL"
        params.currency_code = "EUR"
        communicator = Factory.create_communicator_from_configuration(configuration, metadata_provider=metadata_provider)

        with Factory.create_client_from_communicator(communicator) as client:
            response = client.v1().merchant(MERCHANT_ID).products().directory(809, params)

        self.assertGreater(len(response.entries), 0)


if __name__ == '__main__':
    unittest.main()
