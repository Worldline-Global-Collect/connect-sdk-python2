# -*- coding: utf-8 -*-
#
# This class was auto-generated from the API references found at
# https://apireference.connect.worldline-solutions.com/
#
from worldline.connect.sdk.communication.param_request import ParamRequest
from worldline.connect.sdk.communication.request_param import RequestParam


class FindRefundsParams(ParamRequest):
    """
    Query parameters for Find refunds

    See also https://apireference.connect.worldline-solutions.com/s2sapi/v1/en_US/python/refunds/find.html
    """

    __hosted_checkout_id = None
    __merchant_reference = None
    __merchant_order_id = None
    __offset = None
    __limit = None

    @property
    def hosted_checkout_id(self):
        """
        | Your hosted checkout identifier to filter on.

        Type: str
        """
        return self.__hosted_checkout_id

    @hosted_checkout_id.setter
    def hosted_checkout_id(self, value):
        self.__hosted_checkout_id = value

    @property
    def merchant_reference(self):
        """
        | Your unique transaction reference to filter on.

        Type: str
        """
        return self.__merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, value):
        self.__merchant_reference = value

    @property
    def merchant_order_id(self):
        """
        | Your order identifier to filter on.

        Type: long
        """
        return self.__merchant_order_id

    @merchant_order_id.setter
    def merchant_order_id(self, value):
        self.__merchant_order_id = value

    @property
    def offset(self):
        """
        | The zero-based index of the first refund in the result. If omitted, the offset will be 0.

        Type: int
        """
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def limit(self):
        """
        | The maximum number of refunds to return, with a maximum of 100. If omitted, the limit will be 10.

        Type: int
        """
        return self.__limit

    @limit.setter
    def limit(self, value):
        self.__limit = value

    def to_request_parameters(self):
        """
        :return: list[RequestParam]
        """
        result = []
        if self.hosted_checkout_id is not None:
            result.append(RequestParam("hostedCheckoutId", self.hosted_checkout_id))
        if self.merchant_reference is not None:
            result.append(RequestParam("merchantReference", self.merchant_reference))
        if self.merchant_order_id is not None:
            result.append(RequestParam("merchantOrderId", str(self.merchant_order_id)))
        if self.offset is not None:
            result.append(RequestParam("offset", str(self.offset)))
        if self.limit is not None:
            result.append(RequestParam("limit", str(self.limit)))
        return result
