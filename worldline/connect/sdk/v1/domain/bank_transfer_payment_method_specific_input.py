# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.abstract_bank_transfer_payment_method_specific_input import AbstractBankTransferPaymentMethodSpecificInput


class BankTransferPaymentMethodSpecificInput(AbstractBankTransferPaymentMethodSpecificInput):

    def to_dictionary(self):
        dictionary = super(BankTransferPaymentMethodSpecificInput, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(BankTransferPaymentMethodSpecificInput, self).from_dictionary(dictionary)
        return self
