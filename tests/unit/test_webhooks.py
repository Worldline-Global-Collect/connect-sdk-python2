import unittest

from worldline.connect.sdk.json.default_marshaller import DefaultMarshaller
from worldline.connect.sdk.webhooks.in_memory_secret_key_store import InMemorySecretKeyStore
from worldline.connect.sdk.webhooks.webhooks import Webhooks


class WebhooksTest(unittest.TestCase):
    def test_create_helper(self):
        helper = Webhooks.v1().create_helper(InMemorySecretKeyStore.instance())
        self.assertIs(DefaultMarshaller.instance(), helper.marshaller)
        self.assertIs(InMemorySecretKeyStore.instance(),
                      helper.secret_key_store)


if __name__ == '__main__':
    unittest.main()
