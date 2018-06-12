"""
error.py
 is a module contains schema error exceptions.

        Created on  :   June 10, 2018
        Author      :   Mohammad Alrefai
"""


class SchemaError(Exception):
    """Error during Schema validation."""

    def __init__(self, errors):
        self._errors = errors if type(errors) is list else [errors]
        Exception.__init__(self, self.code)

    @property
    def code(self):
        """
        Removes duplicates values in auto and error list.
        parameters.
        """

        def unique(seq):
            """
            Utility function that removes duplicate.
            """
            seen = set()
            seen_add = seen.add
            # This way removes duplicates while preserving the order.
            return [x for x in seq if x not in seen and not seen_add(x)]

        error_list = unique(i for i in self._errors if i is not None)
        return '\n'.join(error_list)


class SchemaMissingKeyError(SchemaError):
    """Error should be raised when a mandatory key is not found within the
    data set being validated"""
    pass


class SchemaUnexpectedTypeError(SchemaError):
    """Error should be raised when a type mismatch is detected within the
    data set being validated."""
    pass


class SchemaUnrecognizableTypeError(SchemaError):
    """Error Should be raised when an unrecognizable type is detected
    within the given schema structure."""
    pass
