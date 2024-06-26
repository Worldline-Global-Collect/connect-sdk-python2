# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class ApproveRefundRequest(DataObject):

    __amount = None

    @property
    def amount(self):
        """
        | Refund amount to be approved

        Type: long
        """
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    def to_dictionary(self):
        dictionary = super(ApproveRefundRequest, self).to_dictionary()
        if self.amount is not None:
            dictionary['amount'] = self.amount
        return dictionary

    def from_dictionary(self, dictionary):
        super(ApproveRefundRequest, self).from_dictionary(dictionary)
        if 'amount' in dictionary:
            self.amount = dictionary['amount']
        return self
