__title__ = 'popbooks'
__version__ = '0.0.1'
__author__ = 'Joe Gallo'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Joe Gallo'

import json

# get credentials
with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)

AWS_ACCESS_KEY = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = '1234567890' # TODO: credentials['aws_secret_access_key']
AMAZON_ASSOCIATE_ID = credentials['amazon_associate_id']
