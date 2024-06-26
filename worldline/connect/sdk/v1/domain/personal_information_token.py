# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject
from worldline.connect.sdk.v1.domain.personal_name_token import PersonalNameToken


class PersonalInformationToken(DataObject):

    __name = None

    @property
    def name(self):
        """
        | Given name(s) or first name(s) of the customer

        Type: :class:`worldline.connect.sdk.v1.domain.personal_name_token.PersonalNameToken`
        """
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dictionary(self):
        dictionary = super(PersonalInformationToken, self).to_dictionary()
        if self.name is not None:
            dictionary['name'] = self.name.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(PersonalInformationToken, self).from_dictionary(dictionary)
        if 'name' in dictionary:
            if not isinstance(dictionary['name'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['name']))
            value = PersonalNameToken()
            self.name = value.from_dictionary(dictionary['name'])
        return self
