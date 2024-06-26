# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.payment_creation_references import PaymentCreationReferences


class PaymentCreationOutput(PaymentCreationReferences):

    __is_checked_remember_me = None
    __is_new_token = None
    __token = None
    __tokenization_succeeded = None

    @property
    def is_checked_remember_me(self):
        """
        | Indicates whether the customer ticked the "Remember my details for future purchases" checkbox on the MyCheckout hosted payment pages

        Type: bool
        """
        return self.__is_checked_remember_me

    @is_checked_remember_me.setter
    def is_checked_remember_me(self, value):
        self.__is_checked_remember_me = value

    @property
    def is_new_token(self):
        """
        | Indicates if a new token was created
        
        * true - A new token was created
        * false - A token with the same card number already exists and is returned. Please note that the existing token has not been updated. When you want to update other data then the card number, you need to update data stored in the token explicitly, as data is never updated during the creation of a token.

        Type: bool
        """
        return self.__is_new_token

    @is_new_token.setter
    def is_new_token(self, value):
        self.__is_new_token = value

    @property
    def token(self):
        """
        | ID of the token

        Type: str
        """
        return self.__token

    @token.setter
    def token(self, value):
        self.__token = value

    @property
    def tokenization_succeeded(self):
        """
        | Indicates if tokenization was successful or not. If this value is false, then the token and isNewToken properties will not be set.

        Type: bool
        """
        return self.__tokenization_succeeded

    @tokenization_succeeded.setter
    def tokenization_succeeded(self, value):
        self.__tokenization_succeeded = value

    def to_dictionary(self):
        dictionary = super(PaymentCreationOutput, self).to_dictionary()
        if self.is_checked_remember_me is not None:
            dictionary['isCheckedRememberMe'] = self.is_checked_remember_me
        if self.is_new_token is not None:
            dictionary['isNewToken'] = self.is_new_token
        if self.token is not None:
            dictionary['token'] = self.token
        if self.tokenization_succeeded is not None:
            dictionary['tokenizationSucceeded'] = self.tokenization_succeeded
        return dictionary

    def from_dictionary(self, dictionary):
        super(PaymentCreationOutput, self).from_dictionary(dictionary)
        if 'isCheckedRememberMe' in dictionary:
            self.is_checked_remember_me = dictionary['isCheckedRememberMe']
        if 'isNewToken' in dictionary:
            self.is_new_token = dictionary['isNewToken']
        if 'token' in dictionary:
            self.token = dictionary['token']
        if 'tokenizationSucceeded' in dictionary:
            self.tokenization_succeeded = dictionary['tokenizationSucceeded']
        return self
