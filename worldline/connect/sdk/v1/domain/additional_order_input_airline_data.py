# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.airline_data import AirlineData
from worldline.connect.sdk.v1.domain.lodging_data import LodgingData


class AdditionalOrderInputAirlineData(DataObject):

    __airline_data = None
    __lodging_data = None

    @property
    def airline_data(self):
        """
        | Object that holds airline specific data

        Type: :class:`worldline.connect.sdk.v1.domain.airline_data.AirlineData`
        """
        return self.__airline_data

    @airline_data.setter
    def airline_data(self, value):
        self.__airline_data = value

    @property
    def lodging_data(self):
        """
        | Object that holds lodging specific data

        Type: :class:`worldline.connect.sdk.v1.domain.lodging_data.LodgingData`
        """
        return self.__lodging_data

    @lodging_data.setter
    def lodging_data(self, value):
        self.__lodging_data = value

    def to_dictionary(self):
        dictionary = super(AdditionalOrderInputAirlineData, self).to_dictionary()
        if self.airline_data is not None:
            dictionary['airlineData'] = self.airline_data.to_dictionary()
        if self.lodging_data is not None:
            dictionary['lodgingData'] = self.lodging_data.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(AdditionalOrderInputAirlineData, self).from_dictionary(dictionary)
        if 'airlineData' in dictionary:
            if not isinstance(dictionary['airlineData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['airlineData']))
            value = AirlineData()
            self.airline_data = value.from_dictionary(dictionary['airlineData'])
        if 'lodgingData' in dictionary:
            if not isinstance(dictionary['lodgingData'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['lodgingData']))
            value = LodgingData()
            self.lodging_data = value.from_dictionary(dictionary['lodgingData'])
        return self
