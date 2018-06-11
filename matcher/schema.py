"""
schema.py
 is a class for validating transactions.

        Created on  :   June 9, 2018
        Author      :   Mohammad Alrefai
"""


from .validator import Validator
from .error import SchemaError


__version__ = '0.1.0'
__all__ = ['Schema']


class Schema:
    """
    Entry point of the transaction validation library,
    use this class to instantiate validation
    schema for the data that will be validated.
    """

    def __init__(self, schema):
        self._schema = schema
        self._error = []

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._schema)

    def is_valid(self, data):
        """
        Return whether the given data has passed all the validations
        that were specified in the given schema.

        :param data: dictionary
        :return: boolean
        """

        try:
            Validator.check_structure(self._schema, data)
        except SchemaError as e:
            print(e)
            return False
        else:
            return True
