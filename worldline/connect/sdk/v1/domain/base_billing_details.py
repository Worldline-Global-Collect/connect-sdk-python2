# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class BaseBillingDetails(DataObject):

    __description = None

    @property
    def description(self):
        """
        Type: str
        """
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    def to_dictionary(self):
        dictionary = super(BaseBillingDetails, self).to_dictionary()
        if self.description is not None:
            dictionary['description'] = self.description
        return dictionary

    def from_dictionary(self, dictionary):
        super(BaseBillingDetails, self).from_dictionary(dictionary)
        if 'description' in dictionary:
            self.description = dictionary['description']
        return self
