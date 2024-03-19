# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.contact_details_base import ContactDetailsBase


class ContactDetailsToken(ContactDetailsBase):

    def to_dictionary(self):
        dictionary = super(ContactDetailsToken, self).to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(ContactDetailsToken, self).from_dictionary(dictionary)
        return self
