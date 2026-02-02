# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.base_billing_details import BaseBillingDetails


class AutomaticReloadBillingDetails(BaseBillingDetails):
    """
    | An object that contains the reload amount and balance threshold for the automatic reload payment.
    """

    __automatic_reload_payment_threshold_amount = None

    @property
    def automatic_reload_payment_threshold_amount(self):
        """
        | The balance an account reaches for the automatic reload amount to be applied.

        Type: long
        """
        return self.__automatic_reload_payment_threshold_amount

    @automatic_reload_payment_threshold_amount.setter
    def automatic_reload_payment_threshold_amount(self, value):
        self.__automatic_reload_payment_threshold_amount = value

    def to_dictionary(self):
        dictionary = super(AutomaticReloadBillingDetails, self).to_dictionary()
        if self.automatic_reload_payment_threshold_amount is not None:
            dictionary['automaticReloadPaymentThresholdAmount'] = self.automatic_reload_payment_threshold_amount
        return dictionary

    def from_dictionary(self, dictionary):
        super(AutomaticReloadBillingDetails, self).from_dictionary(dictionary)
        if 'automaticReloadPaymentThresholdAmount' in dictionary:
            self.automatic_reload_payment_threshold_amount = dictionary['automaticReloadPaymentThresholdAmount']
        return self
