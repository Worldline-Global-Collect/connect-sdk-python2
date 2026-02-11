# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.click_to_pay_scheme_configuration_base import ClickToPaySchemeConfigurationBase


class ClickToPayConfigurationVisa(ClickToPaySchemeConfigurationBase):
    """
    | Scheme onboarding value returned for the card products supporting Click to Pay with Visa.
    """

    __encryption_key = None
    __n_modulus = None

    @property
    def encryption_key(self):
        """
        | Key ID of the encryption key to encrypt card information before sending it to Visa.

        Type: str
        """
        return self.__encryption_key

    @encryption_key.setter
    def encryption_key(self, value):
        self.__encryption_key = value

    @property
    def n_modulus(self):
        """
        | Modulus of the encryption key to encrypt card information before sending it to Visa.

        Type: str
        """
        return self.__n_modulus

    @n_modulus.setter
    def n_modulus(self, value):
        self.__n_modulus = value

    def to_dictionary(self):
        dictionary = super(ClickToPayConfigurationVisa, self).to_dictionary()
        if self.encryption_key is not None:
            dictionary['encryptionKey'] = self.encryption_key
        if self.n_modulus is not None:
            dictionary['nModulus'] = self.n_modulus
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPayConfigurationVisa, self).from_dictionary(dictionary)
        if 'encryptionKey' in dictionary:
            self.encryption_key = dictionary['encryptionKey']
        if 'nModulus' in dictionary:
            self.n_modulus = dictionary['nModulus']
        return self
