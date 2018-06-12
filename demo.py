"""
demo.py
    is an app demo use the library that validate transactions
        Created on  :   June 9, 2016
        Author      :   Mohammad Alrefai
"""

import json

import validate_transaction


def main():

    args = dict()
    args['schema'] = './demo/files/transactionSchema.json'
    args['data'] = './demo/files/transactionData.json'

    # Read JSON schema into the schema variable
    with open(args['schema']) as f:
        schema = json.load(f)

    # Read JSON data into the data variable
    with open(args['data']) as f:
        data = json.load(f)

    result = "Valid" if validate_transaction.Schema(schema).is_valid(data) else "Invalid"
    print("%s transaction data upon on given schema" % result)

    print('Good Bye !!!')


main()
