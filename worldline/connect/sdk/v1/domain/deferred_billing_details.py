# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.base_billing_details import BaseBillingDetails


class DeferredBillingDetails(BaseBillingDetails):
    """
    | An object that contains details about the deferred payment.
    """

    __deferred_payment_date = None
    __free_cancellation_date = None
    __free_cancellation_date_time_zone = None

    @property
    def deferred_payment_date(self):
        """
        | The date of the payment in in YYYYMMDD format that will take place in the future.

        Type: str
        """
        return self.__deferred_payment_date

    @deferred_payment_date.setter
    def deferred_payment_date(self, value):
        self.__deferred_payment_date = value

    @property
    def free_cancellation_date(self):
        """
        | The date until which customers can cancel their recurring payment without charges in YYYYMMDDHH24MISS format.

        Type: str
        """
        return self.__free_cancellation_date

    @free_cancellation_date.setter
    def free_cancellation_date(self, value):
        self.__free_cancellation_date = value

    @property
    def free_cancellation_date_time_zone(self):
        """
        | The IANA timezone identifier that provides the correct local context for interpreting the free cancellation deadline displayed on the payment sheet.

        Type: str
        """
        return self.__free_cancellation_date_time_zone

    @free_cancellation_date_time_zone.setter
    def free_cancellation_date_time_zone(self, value):
        self.__free_cancellation_date_time_zone = value

    def to_dictionary(self):
        dictionary = super(DeferredBillingDetails, self).to_dictionary()
        if self.deferred_payment_date is not None:
            dictionary['deferredPaymentDate'] = self.deferred_payment_date
        if self.free_cancellation_date is not None:
            dictionary['freeCancellationDate'] = self.free_cancellation_date
        if self.free_cancellation_date_time_zone is not None:
            dictionary['freeCancellationDateTimeZone'] = self.free_cancellation_date_time_zone
        return dictionary

    def from_dictionary(self, dictionary):
        super(DeferredBillingDetails, self).from_dictionary(dictionary)
        if 'deferredPaymentDate' in dictionary:
            self.deferred_payment_date = dictionary['deferredPaymentDate']
        if 'freeCancellationDate' in dictionary:
            self.free_cancellation_date = dictionary['freeCancellationDate']
        if 'freeCancellationDateTimeZone' in dictionary:
            self.free_cancellation_date_time_zone = dictionary['freeCancellationDateTimeZone']
        return self
