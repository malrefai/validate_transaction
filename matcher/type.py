"""
type.py
 is a module contains custom types for data in transaction.

        Created on  :   June 10, 2018
        Author      :   Mohammad Alrefai
"""

import re
from abc import ABC, abstractmethod


class Type(ABC):

    @staticmethod
    def factory(data_type):
        return CUSTOM_TYPES[data_type]()

    @abstractmethod
    def match(self, data):
        pass


class BooleanType(Type):
    def match(self, data):
        return isinstance(data, bool)


class StringType(Type):
    def match(self, data):
        return isinstance(data, str)


class IntegerType(Type):
    def match(self, data):
        return isinstance(data, int)


class FloatType(Type):
    def match(self, data):
        return isinstance(data, float) or isinstance(data, int)


class EmailType(Type):
    PATTERN = r'^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$'

    def match(self, data):
        return isinstance(data, str) and re.match(EmailType.PATTERN, data, re.I)


class CurrencyType(Type):
    # TODO Add more currencies or load them from file
    CURRENCY = {
                   "USD": "United States Dollar",
                   "EUR": "European Euro",
                   "GBP": "The British Pound",
                   "YEN": "Japanese Yen",
                   "JOD": "Jordan Dinar",
                   "EGP": "Egypt Pound",
                   "KWD": "Kuwaiti Dinar"
                }

    def match(self, data):
        return isinstance(data, str) and data.upper() in CurrencyType.CURRENCY.keys()


class TenderType(Type):
    # TODO Add more tender types or load them from file
    TENDER = {
                   "CASH": "Cash Type",
                   "CREDIT": "Credit Type"
             }

    def match(self, data):
        return isinstance(data, str) and data.upper() in TenderType.TENDER.keys()


class InclusionType(Type):
    # TODO Add more inclusion types or load them from file
    INCLUSION = {
                   "INCLUSIVE": "Inclusive Type",
                   "EXCLUSIVE": "Exclusive Type"
                }

    def match(self, data):
        return isinstance(data, str) and data.upper() in InclusionType.INCLUSION.keys()


CUSTOM_TYPES = {
    "bool": BooleanType,
    "boolean": BooleanType,
    "string": StringType,
    "str": StringType,
    "integer": IntegerType,
    "int": IntegerType,
    "float": FloatType,
    "double": FloatType,
    "email": EmailType,
    "currency": CurrencyType,
    "tender": TenderType,
    "inclusion": InclusionType
}
