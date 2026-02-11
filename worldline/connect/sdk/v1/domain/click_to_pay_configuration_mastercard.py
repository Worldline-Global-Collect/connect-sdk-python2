# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.click_to_pay_scheme_configuration_base import ClickToPaySchemeConfigurationBase


class ClickToPayConfigurationMastercard(ClickToPaySchemeConfigurationBase):
    """
    | Scheme onboarding value returned for the card products supporting Click to Pay with Mastercard.
    """

    def to_dictionary(self):
        dictionary = super(ClickToPayConfigurationMastercard, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPayConfigurationMastercard, self).from_dictionary(dictionary)
        return self
