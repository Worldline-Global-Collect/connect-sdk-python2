# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.abstract_mobile_payment_method_specific_input import AbstractMobilePaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.mobile_payment_product302_specific_input_hosted_checkout import MobilePaymentProduct302SpecificInputHostedCheckout
from worldline.connect.sdk.v1.domain.mobile_payment_product320_specific_input_hosted_checkout import MobilePaymentProduct320SpecificInputHostedCheckout


class MobilePaymentMethodSpecificInputHostedCheckout(AbstractMobilePaymentMethodSpecificInput):

    __payment_product302_specific_input = None
    __payment_product320_specific_input = None

    @property
    def payment_product302_specific_input(self):
        """
        | Object containing information specific to Apple Pay

        Type: :class:`worldline.connect.sdk.v1.domain.mobile_payment_product302_specific_input_hosted_checkout.MobilePaymentProduct302SpecificInputHostedCheckout`
        """
        return self.__payment_product302_specific_input

    @payment_product302_specific_input.setter
    def payment_product302_specific_input(self, value):
        self.__payment_product302_specific_input = value

    @property
    def payment_product320_specific_input(self):
        """
        | Object containing information specific to Google Pay (paymentProductId 320)

        Type: :class:`worldline.connect.sdk.v1.domain.mobile_payment_product320_specific_input_hosted_checkout.MobilePaymentProduct320SpecificInputHostedCheckout`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value):
        self.__payment_product320_specific_input = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificInputHostedCheckout, self).to_dictionary()
        if self.payment_product302_specific_input is not None:
            dictionary['paymentProduct302SpecificInput'] = self.payment_product302_specific_input.to_dictionary()
        if self.payment_product320_specific_input is not None:
            dictionary['paymentProduct320SpecificInput'] = self.payment_product320_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificInputHostedCheckout, self).from_dictionary(dictionary)
        if 'paymentProduct302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificInput']))
            value = MobilePaymentProduct302SpecificInputHostedCheckout()
            self.payment_product302_specific_input = value.from_dictionary(dictionary['paymentProduct302SpecificInput'])
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInputHostedCheckout()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        return self
