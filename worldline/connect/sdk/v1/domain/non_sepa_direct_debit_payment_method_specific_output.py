# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.v1.domain.abstract_payment_method_specific_output import AbstractPaymentMethodSpecificOutput
from worldline.connect.sdk.v1.domain.fraud_results import FraudResults


class NonSepaDirectDebitPaymentMethodSpecificOutput(AbstractPaymentMethodSpecificOutput):

    __fraud_results = None

    @property
    def fraud_results(self):
        """
        | Object containing the results of the fraud screening

        Type: :class:`worldline.connect.sdk.v1.domain.fraud_results.FraudResults`
        """
        return self.__fraud_results

    @fraud_results.setter
    def fraud_results(self, value):
        self.__fraud_results = value

    def to_dictionary(self):
        dictionary = super(NonSepaDirectDebitPaymentMethodSpecificOutput, self).to_dictionary()
        if self.fraud_results is not None:
            dictionary['fraudResults'] = self.fraud_results.to_dictionary()
        return dictionary

    def from_dictionary(self, dictionary):
        super(NonSepaDirectDebitPaymentMethodSpecificOutput, self).from_dictionary(dictionary)
        if 'fraudResults' in dictionary:
            if not isinstance(dictionary['fraudResults'], dict):
                raise TypeError('value \'{}\' is not a dictionary'.format(dictionary['fraudResults']))
            value = FraudResults()
            self.fraud_results = value.from_dictionary(dictionary['fraudResults'])
        return self
