"""
validator.py
 is a class for validating data with schema.

        Created on  :   June 9, 2018
        Author      :   Mohammad Alrefai
"""


from .error import SchemaMissingKeyError, SchemaUnexpectedTypeError, SchemaUnrecognizableTypeError
from .type import CUSTOM_TYPES, Type

__version__ = '0.1.0'
__all__ = ['Validator']


class Validator:
    """

    """

    @staticmethod
    def _is_dict(schema, data):
        return isinstance(schema, dict) and isinstance(data, dict)

    @staticmethod
    def _is_list(schema, data):
        return isinstance(schema, list) and isinstance(data, list)

    @staticmethod
    def _is_type(schema):
        return schema.strip().lower() in CUSTOM_TYPES.keys()

    @staticmethod
    def _is_data_match_type(data_type, data):
        return Type.factory(data_type.strip().lower()).match(data)

    @staticmethod
    def check_structure(schema, data):

        if Validator._is_dict(schema, data):
            for key in schema:
                if key not in data:
                    raise SchemaMissingKeyError("Missing key: %s" % key)
                Validator.check_structure(schema[key], data[key])

        elif Validator._is_list(schema, data):
            # schema  is list in the form [type or dict]
            for datum in data:
                Validator.check_structure(schema[0], datum)

        elif Validator._is_type(schema):
            # structure is the type of data
            if not Validator._is_data_match_type(schema, data):
                raise SchemaUnexpectedTypeError(
                    "Mismatch data with type: '%s' is not instance of %s" % (data, schema))

        else:
            # structure is neither a dict, nor list, not TYPES
            raise SchemaUnrecognizableTypeError("Unrecognizable type in schema: %s" % schema)

