# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.abstract_mobile_payment_method_specific_input import AbstractMobilePaymentMethodSpecificInput
from worldline.connect.sdk.v1.domain.decrypted_payment_data import DecryptedPaymentData
from worldline.connect.sdk.v1.domain.mobile_payment_product320_specific_input import MobilePaymentProduct320SpecificInput


class MobilePaymentMethodSpecificInput(AbstractMobilePaymentMethodSpecificInput):

    __decrypted_payment_data = None
    __encrypted_payment_data = None
    __is_recurring = None
    __merchant_initiated_reason_indicator = None
    __payment_product320_specific_input = None

    @property
    def decrypted_payment_data(self):
        """
        | The payment data if you do the decryption of the encrypted payment data yourself.

        Type: :class:`worldline.connect.sdk.v1.domain.decrypted_payment_data.DecryptedPaymentData`
        """
        return self.__decrypted_payment_data

    @decrypted_payment_data.setter
    def decrypted_payment_data(self, value):
        self.__decrypted_payment_data = value

    @property
    def encrypted_payment_data(self):
        """
        | The payment data if we will do the decryption of the encrypted payment data.
        
        
        | Typically you'd use encryptedCustomerInput in the root of the create payment request to provide the encrypted payment data instead.
        
        * For Apple Pay, the encrypted payment data is the PKPayment <https://developer.apple.com/documentation/passkit/pkpayment>.token.paymentData object passed as a string (with all quotation marks escaped).
        * For Google Pay, the encrypted payment data can be found in property paymentMethodData.tokenizationData.token of the PaymentData <https://developers.google.com/android/reference/com/google/android/gms/wallet/PaymentData>.toJson() result.

        Type: str
        """
        return self.__encrypted_payment_data

    @encrypted_payment_data.setter
    def encrypted_payment_data(self, value):
        self.__encrypted_payment_data = value

    @property
    def is_recurring(self):
        """
        | Indicates if this transaction is of a one-off or a recurring type
        
        * true - This is recurring
        * false - This is one-off

        Type: bool
        """
        return self.__is_recurring

    @is_recurring.setter
    def is_recurring(self, value):
        self.__is_recurring = value

    @property
    def merchant_initiated_reason_indicator(self):
        """
        | Indicates reason behind the merchant initiated transaction. These are industry specific.
        | Possible values:
        
        * delayedCharges - Delayed charges are performed to process a supplemental account charge after original services have been rendered and respective payment has been processed. This is typically used in hotel, cruise lines and vehicle rental environments to perform a supplemental payment after the original services are rendered.
        * noShow - Cardholders can use their cards to make a guaranteed reservation with certain merchant segments. A guaranteed reservation ensures that the reservation will be honored and allows a merchant to perform a No Show transaction to charge the cardholder a penalty according to the merchant’s cancellation policy. For merchants that accept token-based payment credentials to guarantee a reservation, it is necessary to perform a customer initiated (Account Verification) at the time of reservation to be able perform a No Show transaction later.

        Type: str
        """
        return self.__merchant_initiated_reason_indicator

    @merchant_initiated_reason_indicator.setter
    def merchant_initiated_reason_indicator(self, value):
        self.__merchant_initiated_reason_indicator = value

    @property
    def payment_product320_specific_input(self):
        """
        | Object containing information specific to Google Pay

        Type: :class:`worldline.connect.sdk.v1.domain.mobile_payment_product320_specific_input.MobilePaymentProduct320SpecificInput`
        """
        return self.__payment_product320_specific_input

    @payment_product320_specific_input.setter
    def payment_product320_specific_input(self, value):
        self.__payment_product320_specific_input = value

    def to_dictionary(self):
        dictionary = super(MobilePaymentMethodSpecificInput, self).to_dictionary()
        if self.decrypted_payment_data is not None:
            dictionary['decryptedPaymentData'] = self.decrypted_payment_data.to_dictionary()
        if self.encrypted_payment_data is not None:
            dictionary['encryptedPaymentData'] = self.encrypted_payment_data
        if self.is_recurring is not None:
            dictionary['isRecurring'] = self.is_recurring
        if self.merchant_initiated_reason_indicator is not None:
            dictionary['merchantInitiatedReasonIndicator'] = self.merchant_initiated_reason_indicator
        if self.payment_product320_specific_input is not None:
            dictionary['paymentProduct320SpecificInput'] = self.payment_product320_specific_input.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(MobilePaymentMethodSpecificInput, self).from_dictionary(dictionary)
        if 'decryptedPaymentData' in dictionary:
            if not isinstance(dictionary['decryptedPaymentData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['decryptedPaymentData']))
            value = DecryptedPaymentData()
            self.decrypted_payment_data = value.from_dictionary(dictionary['decryptedPaymentData'])
        if 'encryptedPaymentData' in dictionary:
            self.encrypted_payment_data = dictionary['encryptedPaymentData']
        if 'isRecurring' in dictionary:
            self.is_recurring = dictionary['isRecurring']
        if 'merchantInitiatedReasonIndicator' in dictionary:
            self.merchant_initiated_reason_indicator = dictionary['merchantInitiatedReasonIndicator']
        if 'paymentProduct320SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct320SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct320SpecificInput']))
            value = MobilePaymentProduct320SpecificInput()
            self.payment_product320_specific_input = value.from_dictionary(dictionary['paymentProduct320SpecificInput'])
        return self
