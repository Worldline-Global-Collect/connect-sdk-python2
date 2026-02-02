# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.base_billing_details import BaseBillingDetails


class RecurringBillingDetails(BaseBillingDetails):
    """
    | An object that contains the regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.
    """

    def to_dictionary(self):
        dictionary = super(RecurringBillingDetails, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(RecurringBillingDetails, self).from_dictionary(dictionary)
        return self
