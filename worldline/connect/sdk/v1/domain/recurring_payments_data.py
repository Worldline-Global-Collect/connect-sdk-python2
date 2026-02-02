# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.frequency import Frequency
from worldline.connect.sdk.v1.domain.payment_product302_specific_input import PaymentProduct302SpecificInput
from worldline.connect.sdk.v1.domain.trial_information import TrialInformation


class RecurringPaymentsData(DataObject):
    """
    | The object containing reference data for the text that can be displayed on MyCheckout hosted payment page with subscription information.
    
    | Note:
    
    | The data in this object is only meant for displaying recurring payments-related data on your checkout page.
    | You still need to submit all the recurring payment-related data in the corresponding payment product-specific input. (example: cardPaymentMethodSpecificInput.recurring and cardPaymentMethodSpecificInput.isRecurring)
    """

    __payment_product302_specific_input = None
    __recurring_end_date = None
    __recurring_interval = None
    __recurring_start_date = None
    __trial_information = None

    @property
    def payment_product302_specific_input(self):
        """
        | The object containing information specific to Apple Pay

        Type: :class:`worldline.connect.sdk.v1.domain.payment_product302_specific_input.PaymentProduct302SpecificInput`
        """
        return self.__payment_product302_specific_input

    @payment_product302_specific_input.setter
    def payment_product302_specific_input(self, value):
        self.__payment_product302_specific_input = value

    @property
    def recurring_end_date(self):
        """
        | The date that the recurring payment ends in YYYYMMDD format.

        Type: str
        """
        return self.__recurring_end_date

    @recurring_end_date.setter
    def recurring_end_date(self, value):
        self.__recurring_end_date = value

    @property
    def recurring_interval(self):
        """
        | The object containing the frequency and interval between recurring payments.

        Type: :class:`worldline.connect.sdk.v1.domain.frequency.Frequency`
        """
        return self.__recurring_interval

    @recurring_interval.setter
    def recurring_interval(self, value):
        self.__recurring_interval = value

    @property
    def recurring_start_date(self):
        """
        | The date that the first recurring payment starts in YYYYMMDD format.

        Type: str
        """
        return self.__recurring_start_date

    @recurring_start_date.setter
    def recurring_start_date(self, value):
        self.__recurring_start_date = value

    @property
    def trial_information(self):
        """
        | The object containing data of the trial period: no-cost or discounted time-constrained trial subscription period. 

        Type: :class:`worldline.connect.sdk.v1.domain.trial_information.TrialInformation`
        """
        return self.__trial_information

    @trial_information.setter
    def trial_information(self, value):
        self.__trial_information = value

    def to_dictionary(self):
        dictionary = super(RecurringPaymentsData, self).to_dictionary()
        if self.payment_product302_specific_input is not None:
            dictionary['paymentProduct302SpecificInput'] = self.payment_product302_specific_input.to_dictionary()
        if self.recurring_end_date is not None:
            dictionary['recurringEndDate'] = self.recurring_end_date
        if self.recurring_interval is not None:
            dictionary['recurringInterval'] = self.recurring_interval.to_dictionary()
        if self.recurring_start_date is not None:
            dictionary['recurringStartDate'] = self.recurring_start_date
        if self.trial_information is not None:
            dictionary['trialInformation'] = self.trial_information.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RecurringPaymentsData, self).from_dictionary(dictionary)
        if 'paymentProduct302SpecificInput' in dictionary:
            if not isinstance(dictionary['paymentProduct302SpecificInput'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['paymentProduct302SpecificInput']))
            value = PaymentProduct302SpecificInput()
            self.payment_product302_specific_input = value.from_dictionary(dictionary['paymentProduct302SpecificInput'])
        if 'recurringEndDate' in dictionary:
            self.recurring_end_date = dictionary['recurringEndDate']
        if 'recurringInterval' in dictionary:
            if not isinstance(dictionary['recurringInterval'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['recurringInterval']))
            value = Frequency()
            self.recurring_interval = value.from_dictionary(dictionary['recurringInterval'])
        if 'recurringStartDate' in dictionary:
            self.recurring_start_date = dictionary['recurringStartDate']
        if 'trialInformation' in dictionary:
            if not isinstance(dictionary['trialInformation'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['trialInformation']))
            value = TrialInformation()
            self.trial_information = value.from_dictionary(dictionary['trialInformation'])
        return self
