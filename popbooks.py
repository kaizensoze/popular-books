
import base64
import hashlib
import hmac
import urllib.parse

secret_key = b'1234567890'

f = open('test_request.txt', 'rb')
try:
    body = f.read()
finally:
    f.close()

digest = hmac.new(secret_key, body, hashlib.sha256).digest()
decoded_digest = base64.b64encode(digest).decode()
urlencoded_decoded_digest = urllib.parse.quote_plus(decoded_digest)
print(urlencoded_decoded_digest)
