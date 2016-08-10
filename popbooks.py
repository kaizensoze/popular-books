
import base64
import datetime
import hashlib
import hmac
import json
import requests
import time
import urllib.parse

# # get aws credentials
# with open('credentials.json') as credentials_file:
#     credentials = json.load(credentials_file)
# 
# AWS_ACCESS_KEY = credentials['aws_access_key_id']
# AWS_SECRET_ACCESS_KEY = '1234567890' # TODO: credentials['aws_secret_access_key']
# 
# # generate Signature param [for test request]
# urlParts = {
#     'method': "GET",
#     'protocol': "http",
#     'domain': "webservices.amazon.com",
#     'path': "/onca/xml",
#     'params': [
#         "Service=AWSECommerceService",
#         "AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE",
#         "AssociateTag=mytag-20",
#         "Operation=ItemLookup",
#         "ItemId=0679722769",
#         "ResponseGroup=Images,ItemAttributes,Offers,Reviews",
#         "Version=2013-08-01",
#         "Timestamp=2014-08-18T12:00:00Z"
#     ]
# }
# signatureSeedString = "\n".join([
#     urlParts['method'],
#     urlParts['domain'],
#     urlParts['path'],
#     urllib.parse.quote("&".join(sorted(urlParts['params'])), safe='=&')
# ])
# print(signatureSeedString, "\n")
# 
# # compare with test file
# with open('test_request.txt', 'r') as test_request_file:
#     test_request_contents = test_request_file.read()
# print(test_request_contents)
# 
# digest = hmac.new(str.encode(AWS_SECRET_ACCESS_KEY), msg=str.encode(signatureSeedString), digestmod=hashlib.sha256).digest()
# decoded_digest = base64.b64encode(digest).decode()
# urlencoded_decoded_digest = urllib.parse.quote_plus(decoded_digest)
# print(urlencoded_decoded_digest)

# url = (
#     urlParts["protocol"] + "://" + urlParts["domain"] + urlParts["path"] + "?"
# )
# first = True
# for param in urlParts["params"]:
#     if not first:
#         url += "&"
#     url += param
#     first = False
# print(url)

def generate_timestamp():
    """ Generates timestamp of the format 2014-08-18T12:00:00Z. """
    now = time.time()
    ts = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%dT%H:%M:%SZ')
    return ts
