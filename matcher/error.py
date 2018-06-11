"""
error.py
 is a class for validating schema with data.

        Created on  :   June 10, 2018
        Author      :   Mohammad Alrefai
"""


class SchemaError(Exception):
    """Error during Schema validation."""

    def __init__(self, autos, errors=None):
        self.autos = autos if type(autos) is list else [autos]
        self.errors = errors if type(errors) is list else [errors]
        Exception.__init__(self, self.code)

    @property
    def code(self):
        """
        Removes duplicates values in auto and error list.
        parameters.
        """
        def uniq(seq):
            """
            Utility function that removes duplicate.
            """
            seen = set()
            seen_add = seen.add
            # This way removes duplicates while preserving the order.
            return [x for x in seq if x not in seen and not seen_add(x)]
        data_set = uniq(i for i in self.autos if i is not None)
        error_list = uniq(i for i in self.errors if i is not None)
        if error_list:
            return '\n'.join(error_list)
        return '\n'.join(data_set)


class SchemaMissingKeyError(SchemaError):
    """Error should be raised when a mandatory key is not found within the
    data set being validated"""
    pass


class SchemaUnexpectedTypeError(SchemaError):
    """Error should be raised when a type mismatch is detected within the
    data set being validated."""
    pass


class DataUnmatchedTypeError(SchemaError):
    """Error Should be raised when a datum is not matched within the type.
    """
    pass
