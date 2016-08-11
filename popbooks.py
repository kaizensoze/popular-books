
import popbooks.util as util

# TODO: replace with non-test url
url = (
    "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&AWS"
    "AccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&Operation=ItemL"
    "ookup&ItemId=0679722769&ResponseGroup=Images,ItemAttributes,Offers,Rev"
    "iews&Version=2013-08-01&Timestamp=2014-08-18T12:00:00Z"
)
url = util.url_with_timestamp(url)
url = util.url_with_signature(url)
print(url)

# TODO: use requests to make a request, check response