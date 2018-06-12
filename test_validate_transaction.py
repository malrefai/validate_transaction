from validate_transaction.schema import Schema
from validate_transaction.validator import Validator
from validate_transaction.error import SchemaError
from validate_transaction.error import SchemaUnrecognizableTypeError
from validate_transaction.error import SchemaUnexpectedTypeError
from validate_transaction.error import SchemaMissingKeyError

# Specs for Schema(schema).is_valid method

transaction_schema = {
    '_id': 'string',
    'business_id': 'String',
    'location_id': 'string',
    'transaction_id': 'string',
    'receipt_id': 'string',
    'serial_number': 'string',
    'dining_option': 'string',
    'discount_money': {'amount': 'float', 'currency': 'currency'},
    'emails': ['email']
}

transaction_data = {
    '_id': '589c493e5f2687111bb6d800',
    'business_id': '3f522ee8-7e69-4d78-aeb5-5278aaf21558',
    'location_id': '96e9975b-b1bf-47ee-aeaf-63518022e95e',
    'transaction_id': '37a5f57a-48bc-483d-91b7-88c8b1b9509c',
    'receipt_id': 'Cj9uohMQNVflSq7taYtVRk',
    'serial_number': 'C1-498',
    'dining_option': 'In-House',
    'discount_money': {'amount': 0, 'currency': 'JOD'},
    'emails': ['alrefai@mail.com', 'mohammad@mail.com']
}


def test_is_valid_when_valid_schema_and_data():

    s = Schema(transaction_schema)
    result = s.is_valid(transaction_data)
    assert result == True


def test_is_valid_when_invalid_schema():

    invalid_transaction_schema = {
        '_id': 'string',
        'business_id': 'String',
        'location_id': 'string',
        'transaction_id': 'string',
        'receipt_id': 'string',
        'serial_number': 'string',
        'dining_option': 'string',
        'discount_money': {'amount': 'float', 'currency': 'currency'},
        'email': 'invalid_type'
    }

    s = Schema(invalid_transaction_schema)
    result = s.is_valid(transaction_data)
    assert result == False


def test_is_valid_when_invalid_data():

    invalid_transaction_data = {
        '_id': '589c493e5f2687111bb6d800',
        'business_id': '3f522ee8-7e69-4d78-aeb5-5278aaf21558',
        'location_id': '96e9975b-b1bf-47ee-aeaf-63518022e95e',
        'transaction_id': '37a5f57a-48bc-483d-91b7-88c8b1b9509c',
        'receipt_id': 'Cj9uohMQNVflSq7taYtVRk',
        'serial_number': 'C1-498',
        'dining_option': 'In-House',
        'discount_money': {'amount': 0, 'currency': 'JOD'},
        'email': 'invalid_email'
    }

    s = Schema(transaction_schema)
    result = s.is_valid(invalid_transaction_data)
    assert result == False

# Specs for Validator._is_dict method

dic_schema = {
    'discount_money': {'amount': 'float', 'currency': 'currency'},
    'email': 'email'
}

dic_data = {
    'discount_money': {'amount': 0, 'currency': 'JOD'},
    'email': 'alrefai@mail.com'
}


def test_is_dict_when_valid_schema_and_data():

    result = Validator._is_dict(dic_schema, dic_data)
    assert result == True


def test_is_dict_when_invalid_schema():

    invalid_dic_schema = 'Invalid_dictionary_schema'
    result = Validator._is_dict(invalid_dic_schema, dic_data)
    assert result == False


def test_is_dict_when_invalid_data():

    invalid_dic_data = 'Invalid_dictionary_data'
    result = Validator._is_dict(dic_schema, invalid_dic_data)
    assert result == False


# Specs for Validator._is_list method

list_schema = ['email']
list_data = ['alrefai@mail.com', 'mohammad@mail.com']


def test_is_list_when_valid_schema_and_data():

    result = Validator._is_list(list_schema, list_data)
    assert result == True


def test_is_list_when_invalid_schema():

    invalid_list_schema = 'Invalid_list_schema'
    result = Validator._is_list(invalid_list_schema, list_data)
    assert result == False


def test_is_list_when_invalid_data():

    invalid_list_data = 'Invalid_list_data'
    result = Validator._is_list(list_schema, invalid_list_data)
    assert result == False


# Specs for Validator._is_type method

def test_is_type_when_valid_type():

    valid_type = 'currency'
    result = Validator._is_type(valid_type)
    assert result == True


def test_is_list_when_invalid_type():

    invalid_type = 'invalid_type'
    result = Validator._is_type(invalid_type)
    assert result == False


# Specs for Validator._is_data_match_type method

def test_is_data_match_type_when_data_match_type():

    data_type = 'currency'
    data = 'USD'
    result = Validator._is_data_match_type(data_type, data)
    assert result == True


def test_is_data_match_type_when_data_not_match_type():

    data_type = 'email'
    data = 'invalid_email'
    result = Validator._is_data_match_type(data_type, data)
    assert result == None


# Specs for Validator.check_structure method

schema = {'amount': 'float', 'currency': 'currency'}
data = {'amount': 22.5, 'currency': 'JOD'}


def test_check_structure_when_valid_schema_and_data():

    try:
        Validator.check_structure(schema, data)
    except SchemaError:
        assert False
    else:
        assert True


def test_check_structure_when_schema_has_unrecognizable_type():

    schema_unrecognizable_type = {'amount': 'unrecognizable_type', 'currency': 'currency'}
    try:
        Validator.check_structure(schema_unrecognizable_type, data)
    except SchemaUnrecognizableTypeError:
        assert True
    else:
        assert False


def test_check_structure_when_data_not_match_type():

    data_unexpected_type = {'amount': '22.5', 'currency': 'JOD'}
    try:
        Validator.check_structure(schema, data_unexpected_type)
    except SchemaUnexpectedTypeError:
        assert True
    else:
        assert False


def test_check_structure_when_data_missing_key():

    data_missing_key = {'amount': 22.5}
    try:
        Validator.check_structure(schema, data_missing_key)
    except SchemaMissingKeyError:
        assert True
    else:
        assert False
