# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.click_to_pay_configuration_mastercard import ClickToPayConfigurationMastercard
from worldline.connect.sdk.v1.domain.click_to_pay_configuration_visa import ClickToPayConfigurationVisa


class ClickToPayConfiguration(DataObject):
    """
    | Object containing the configuration parameters for each scheme supporting Click to Pay for the provided country and currency combination. These parameters initialize SRC System SDK for the scheme. This object is only returned for card products with allowsClickToPay set to true.
    """

    __mastercard = None
    __visa = None

    @property
    def mastercard(self):
        """
        | Scheme onboarding value returned for the card products supporting Click to Pay with Mastercard.

        Type: :class:`worldline.connect.sdk.v1.domain.click_to_pay_configuration_mastercard.ClickToPayConfigurationMastercard`
        """
        return self.__mastercard

    @mastercard.setter
    def mastercard(self, value):
        self.__mastercard = value

    @property
    def visa(self):
        """
        | Scheme onboarding value returned for the card products supporting Click to Pay with Visa.

        Type: :class:`worldline.connect.sdk.v1.domain.click_to_pay_configuration_visa.ClickToPayConfigurationVisa`
        """
        return self.__visa

    @visa.setter
    def visa(self, value):
        self.__visa = value

    def to_dictionary(self):
        dictionary = super(ClickToPayConfiguration, self).to_dictionary()
        if self.mastercard is not None:
            dictionary['mastercard'] = self.mastercard.to_dictionary()
        if self.visa is not None:
            dictionary['visa'] = self.visa.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPayConfiguration, self).from_dictionary(dictionary)
        if 'mastercard' in dictionary:
            if not isinstance(dictionary['mastercard'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['mastercard']))
            value = ClickToPayConfigurationMastercard()
            self.mastercard = value.from_dictionary(dictionary['mastercard'])
        if 'visa' in dictionary:
            if not isinstance(dictionary['visa'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['visa']))
            value = ClickToPayConfigurationVisa()
            self.visa = value.from_dictionary(dictionary['visa'])
        return self
