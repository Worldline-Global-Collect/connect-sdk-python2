# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class ClickToPayInput(DataObject):
    """
    | Object holding data that is required to process card transaction with Click to Pay.
    """

    __checkout_response_signature = None

    @property
    def checkout_response_signature(self):
        """
        | The checkoutResponseSignature is a token (JWS) that signs the Checkout response returned by the SRC System after a successful Click to Pay payment. It is used to call the Click to Pay SRCI Server Payload API.

        Type: str
        """
        return self.__checkout_response_signature

    @checkout_response_signature.setter
    def checkout_response_signature(self, value):
        self.__checkout_response_signature = value

    def to_dictionary(self):
        dictionary = super(ClickToPayInput, self).to_dictionary()
        if self.checkout_response_signature is not None:
            dictionary['checkoutResponseSignature'] = self.checkout_response_signature
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPayInput, self).from_dictionary(dictionary)
        if 'checkoutResponseSignature' in dictionary:
            self.checkout_response_signature = dictionary['checkoutResponseSignature']
        return self
