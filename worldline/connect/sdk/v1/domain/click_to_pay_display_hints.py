# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.domain.data_object import DataObject


class ClickToPayDisplayHints(DataObject):

    __logo = None

    @property
    def logo(self):
        """
        | Partial URL that you can reference for the image of Click to Pay. You can use our server-side resize functionality by appending '?size={{width}}x{{height}}' to the full URL, where width and height are specified in pixels. The resized image will always keep its correct aspect ratio.

        Type: str
        """
        return self.__logo

    @logo.setter
    def logo(self, value):
        self.__logo = value

    def to_dictionary(self):
        dictionary = super(ClickToPayDisplayHints, self).to_dictionary()
        if self.logo is not None:
            dictionary['logo'] = self.logo
        return dictionary

    def from_dictionary(self, dictionary):
        super(ClickToPayDisplayHints, self).from_dictionary(dictionary)
        if 'logo' in dictionary:
            self.logo = dictionary['logo']
        return self
