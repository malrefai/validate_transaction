"""
demo.py

        Created on  :   June 9, 2016
        Author      :   Mohammad Alrefai
"""

import json

from matcher import Schema


def main():

    args = dict()
    args['schema'] = './demo/transactionSchemaTest.json'
    args['file'] = './demo/transactionDataTest.json'

    # Read JSON schema into the schema variable
    with open(args['schema']) as f:
        schema = json.load(f)

    # Read JSON data into the data variable
    with open(args['file']) as f:
        data = json.load(f)

    result = "valid" if Schema(schema).is_valid(data) else "invalid"
    print("The transaction data is %s upon given schema" % result)

    print('Good Bye !!!')


main()
