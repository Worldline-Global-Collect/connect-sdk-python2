# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class AbstractRedirectPaymentProduct838SpecificInput(DataObject):

    __network_data = None
    __network_session_token = None

    @property
    def network_data(self):
        """
        Type: str
        """
        return self.__network_data

    @network_data.setter
    def network_data(self, value):
        self.__network_data = value

    @property
    def network_session_token(self):
        """
        Type: str
        """
        return self.__network_session_token

    @network_session_token.setter
    def network_session_token(self, value):
        self.__network_session_token = value

    def to_dictionary(self):
        dictionary = super(AbstractRedirectPaymentProduct838SpecificInput, self).to_dictionary()
        if self.network_data is not None:
            dictionary['networkData'] = self.network_data
        if self.network_session_token is not None:
            dictionary['networkSessionToken'] = self.network_session_token
        return dictionary

    def from_dictionary(self, dictionary):
        super(AbstractRedirectPaymentProduct838SpecificInput, self).from_dictionary(dictionary)
        if 'networkData' in dictionary:
            self.network_data = dictionary['networkData']
        if 'networkSessionToken' in dictionary:
            self.network_session_token = dictionary['networkSessionToken']
        return self
