
import base64
import hashlib
import hmac
import json
import urllib.parse

# get aws credentials
with open('credentials.json') as credentials_file:
    credentials = json.load(credentials_file)

if not credentials:
    raise RuntimeError('Cannot find credentials.json')

AWS_ACCESS_KEY = credentials['aws_access_key_id']
AWS_SECRET_ACCESS_KEY = credentials['aws_secret_access_key']

# generate Signature param for test request
with open('test_request.txt', 'rb') as test_request_file:
    test_request_contents = test_request_file.read()

if not test_request_contents:
    raise RuntimeError('Cannot find test_request.txt')

digest = hmac.new(str.encode('1234567890'), msg=test_request_contents, digestmod=hashlib.sha256).digest()
decoded_digest = base64.b64encode(digest).decode()
urlencoded_decoded_digest = urllib.parse.quote_plus(decoded_digest)
print(urlencoded_decoded_digest)
