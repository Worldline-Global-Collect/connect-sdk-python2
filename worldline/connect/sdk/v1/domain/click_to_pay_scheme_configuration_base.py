# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class ClickToPaySchemeConfigurationBase(DataObject):

    __src_dpa_id = None
    __src_initiator_id = None

    @property
    def src_dpa_id(self):
        """
        Type: str
        """
        return self.__src_dpa_id

    @src_dpa_id.setter
    def src_dpa_id(self, value):
        self.__src_dpa_id = value

    @property
    def src_initiator_id(self):
        """
        Type: str
        """
        return self.__src_initiator_id

    @src_initiator_id.setter
    def src_initiator_id(self, value):
        self.__src_initiator_id = value

    def to_dictionary(self):
        dictionary = super(ClickToPaySchemeConfigurationBase, self).to_dictionary()
        if self.src_dpa_id is not None:
            dictionary['srcDpaId'] = self.src_dpa_id
        if self.src_initiator_id is not None:
            dictionary['srcInitiatorId'] = self.src_initiator_id
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPaySchemeConfigurationBase, self).from_dictionary(dictionary)
        if 'srcDpaId' in dictionary:
            self.src_dpa_id = dictionary['srcDpaId']
        if 'srcInitiatorId' in dictionary:
            self.src_initiator_id = dictionary['srcInitiatorId']
        return self
