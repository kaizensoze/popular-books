
import json

import datetime
import time

from urllib.parse import (urlparse, parse_qs, urlencode, quote, quote_plus, 
    unquote)

from collections import OrderedDict

import base64
import hashlib
import hmac

# get aws credentials
with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)

AWS_ACCESS_KEY = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = '1234567890' # TODO: credentials['aws_secret_access_key']
AMAZON_ASSOCIATE_ID = credentials['amazon_associate_id']

def generate_timestamp():
    """ Generates timestamp of the format 2014-08-18T12:00:00Z. """
    now = time.time()
    ts = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%dT%H:%M:%SZ')
    return ts

def generate_signature(url):
    url_parts = urlparse(url)
    
    # sort query params
    query_params = parse_qs(url_parts.query)
    od = OrderedDict(sorted(query_params.items()))
    
    signature_seed_string = "\n".join([
        'GET',
        url_parts.netloc,
        url_parts.path,
        urlencode(od, doseq=True)
    ])
    print(signature_seed_string, "\n")
    
    # compare with test file
    with open('test_request.txt', 'r') as test_request_file:
        test_request_contents = test_request_file.read()
    print(test_request_contents, "\n")
    
    digest = hmac.new(
        str.encode(AWS_SECRET_ACCESS_KEY),
        msg=str.encode(signature_seed_string),
        digestmod=hashlib.sha256
    ).digest()
    decoded_digest = base64.b64encode(digest).decode()
    urlencoded_decoded_digest = quote_plus(decoded_digest)
    return urlencoded_decoded_digest

def url_with_timestamp(url):
    url_parts = urlparse(url)
    query_params = parse_qs(url_parts.query)
    if 'Timestamp' not in query_params:
        query_params['Timestamp'] = generate_timestamp()
        url_parts = url_parts._replace(
            query = urlencode(query_params, doseq=True)
        )
    return unquote(url_parts.geturl())
    
def url_with_signature(url):
    url_parts = urlparse(url)
    query_params = parse_qs(url_parts.query)
    query_params['Signature'] = generate_signature(url)
    url_parts = url_parts._replace(query = urlencode(query_params, doseq=True))
    return unquote(url_parts.geturl())
