# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.bank_account_bban import BankAccountBban


class TokenNonSepaDirectDebitPaymentProduct730SpecificData(DataObject):

    __bank_account_bban = None

    @property
    def bank_account_bban(self):
        """
        | Object containing account holder name and bank account information

        Type: :class:`worldline.connect.sdk.v1.domain.bank_account_bban.BankAccountBban`
        """
        return self.__bank_account_bban

    @bank_account_bban.setter
    def bank_account_bban(self, value):
        self.__bank_account_bban = value

    def to_dictionary(self):
        dictionary = super(TokenNonSepaDirectDebitPaymentProduct730SpecificData, self).to_dictionary()
        if self.bank_account_bban is not None:
            dictionary['bankAccountBban'] = self.bank_account_bban.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(TokenNonSepaDirectDebitPaymentProduct730SpecificData, self).from_dictionary(dictionary)
        if 'bankAccountBban' in dictionary:
            if not isinstance(dictionary['bankAccountBban'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['bankAccountBban']))
            value = BankAccountBban()
            self.bank_account_bban = value.from_dictionary(dictionary['bankAccountBban'])
        return self
