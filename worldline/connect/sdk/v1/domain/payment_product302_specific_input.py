# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.automatic_reload_billing_details import AutomaticReloadBillingDetails
from worldline.connect.sdk.v1.domain.deferred_billing_details import DeferredBillingDetails
from worldline.connect.sdk.v1.domain.recurring_billing_details import RecurringBillingDetails


class PaymentProduct302SpecificInput(DataObject):

    __automatic_reload_billing = None
    __billing_agreement = None
    __deferred_billing = None
    __management_url = None
    __payment_description = None
    __regular_billing = None
    __token_notification_url = None
    __trial_billing = None

    @property
    def automatic_reload_billing(self):
        """
        | An object that contains the reload amount and balance threshold for the automatic reload payment.

        Type: :class:`worldline.connect.sdk.v1.domain.automatic_reload_billing_details.AutomaticReloadBillingDetails`
        """
        return self.__automatic_reload_billing

    @automatic_reload_billing.setter
    def automatic_reload_billing(self, value):
        self.__automatic_reload_billing = value

    @property
    def billing_agreement(self):
        """
        | A localized description shown to inform the user about the billing terms before authorization. It can include details or conditions of payment, and may describe how customer can cancel payments. 

        Type: str
        """
        return self.__billing_agreement

    @billing_agreement.setter
    def billing_agreement(self, value):
        self.__billing_agreement = value

    @property
    def deferred_billing(self):
        """
        | An object that contains details about the deferred payment.

        Type: :class:`worldline.connect.sdk.v1.domain.deferred_billing_details.DeferredBillingDetails`
        """
        return self.__deferred_billing

    @deferred_billing.setter
    def deferred_billing(self, value):
        self.__deferred_billing = value

    @property
    def management_url(self):
        """
        | A URL to a web page where the customer can update or delete the payment method for the recurring, deferred or automatic reload payment made with Apple Pay.

        Type: str
        """
        return self.__management_url

    @management_url.setter
    def management_url(self, value):
        self.__management_url = value

    @property
    def payment_description(self):
        """
        | The description of the payment used to identify the transaction purpose.

        Type: str
        """
        return self.__payment_description

    @payment_description.setter
    def payment_description(self, value):
        self.__payment_description = value

    @property
    def regular_billing(self):
        """
        | An object that contains the regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.

        Type: :class:`worldline.connect.sdk.v1.domain.recurring_billing_details.RecurringBillingDetails`
        """
        return self.__regular_billing

    @regular_billing.setter
    def regular_billing(self, value):
        self.__regular_billing = value

    @property
    def token_notification_url(self):
        """
        | A URL you provide to receive life-cycle notifications from the Apple Pay servers about the Apple Pay merchant token for the recurring payment. 

        Type: str
        """
        return self.__token_notification_url

    @token_notification_url.setter
    def token_notification_url(self, value):
        self.__token_notification_url = value

    @property
    def trial_billing(self):
        """
        | An object that contains the trial billing cycle for the recurring payment.

        Type: :class:`worldline.connect.sdk.v1.domain.recurring_billing_details.RecurringBillingDetails`
        """
        return self.__trial_billing

    @trial_billing.setter
    def trial_billing(self, value):
        self.__trial_billing = value

    def to_dictionary(self):
        dictionary = super(PaymentProduct302SpecificInput, self).to_dictionary()
        if self.automatic_reload_billing is not None:
            dictionary['automaticReloadBilling'] = self.automatic_reload_billing.to_dictionary()
        if self.billing_agreement is not None:
            dictionary['billingAgreement'] = self.billing_agreement
        if self.deferred_billing is not None:
            dictionary['deferredBilling'] = self.deferred_billing.to_dictionary()
        if self.management_url is not None:
            dictionary['managementUrl'] = self.management_url
        if self.payment_description is not None:
            dictionary['paymentDescription'] = self.payment_description
        if self.regular_billing is not None:
            dictionary['regularBilling'] = self.regular_billing.to_dictionary()
        if self.token_notification_url is not None:
            dictionary['tokenNotificationUrl'] = self.token_notification_url
        if self.trial_billing is not None:
            dictionary['trialBilling'] = self.trial_billing.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentProduct302SpecificInput, self).from_dictionary(dictionary)
        if 'automaticReloadBilling' in dictionary:
            if not isinstance(dictionary['automaticReloadBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['automaticReloadBilling']))
            value = AutomaticReloadBillingDetails()
            self.automatic_reload_billing = value.from_dictionary(dictionary['automaticReloadBilling'])
        if 'billingAgreement' in dictionary:
            self.billing_agreement = dictionary['billingAgreement']
        if 'deferredBilling' in dictionary:
            if not isinstance(dictionary['deferredBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['deferredBilling']))
            value = DeferredBillingDetails()
            self.deferred_billing = value.from_dictionary(dictionary['deferredBilling'])
        if 'managementUrl' in dictionary:
            self.management_url = dictionary['managementUrl']
        if 'paymentDescription' in dictionary:
            self.payment_description = dictionary['paymentDescription']
        if 'regularBilling' in dictionary:
            if not isinstance(dictionary['regularBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['regularBilling']))
            value = RecurringBillingDetails()
            self.regular_billing = value.from_dictionary(dictionary['regularBilling'])
        if 'tokenNotificationUrl' in dictionary:
            self.token_notification_url = dictionary['tokenNotificationUrl']
        if 'trialBilling' in dictionary:
            if not isinstance(dictionary['trialBilling'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['trialBilling']))
            value = RecurringBillingDetails()
            self.trial_billing = value.from_dictionary(dictionary['trialBilling'])
        return self
