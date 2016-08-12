
import datetime
import time

from urllib.parse import (urlparse, parse_qs, urlencode, quote, quote_plus, 
    unquote)

from collections import OrderedDict

import base64
import hashlib
import hmac

from popbooks.settings import (
    AWS_ACCESS_KEY,
    AWS_SECRET_ACCESS_KEY,
    AMAZON_ASSOCIATE_ID
)

def generate_timestamp():
    """ Generates timestamp of the format 2014-08-18T12:00:00Z. """
    now = datetime.datetime.utcnow()
    ts = now.strftime('%Y-%m-%dT%H:%M:%SZ')
    return ts

def generate_signature(url, override_key=None):
    url_parts = urlparse(url)
    
    # sort query params
    query_params = parse_qs(url_parts.query)
    [value.sort() for key, value in query_params.items()] # sort array values
    od = OrderedDict(sorted(query_params.items()))
    
    signature_seed_string = "\n".join([
        'GET',
        url_parts.netloc,
        url_parts.path,
        urlencode(od, doseq=True, quote_via=quote)
    ])
    # print(signature_seed_string, "\n")
    
    key = override_key if override_key else AWS_SECRET_ACCESS_KEY
    digest = hmac.new(
        key=str.encode(key),
        msg=str.encode(signature_seed_string),
        digestmod=hashlib.sha256
    ).digest()
    decoded_digest = base64.b64encode(digest).decode()
    urlencoded_decoded_digest = quote_plus(decoded_digest)
    return urlencoded_decoded_digest

def fill_in_url(url):
    params_to_add = {
        'AWSAccessKeyId': AWS_ACCESS_KEY,
        'AssociateTag': AMAZON_ASSOCIATE_ID,
        'Timestamp': generate_timestamp(),
    }
    
    url_parts = urlparse(url)
    query_params = parse_qs(url_parts.query)
    
    for key, val in params_to_add.items():
        if key not in query_params:
            query_params[key] = val
            url_parts = url_parts._replace(query = urlencode(query_params, doseq=True))
    
    # add signature
    query_params['Signature'] = generate_signature(url_parts.geturl()) # override_key='1234567890'
    url_parts = url_parts._replace(query = urlencode(query_params, doseq=True))
    
    return unquote(url_parts.geturl())
