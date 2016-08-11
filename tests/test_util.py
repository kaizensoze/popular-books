
import json
import pytest
from popbooks.util import generate_signature

class TestGenerateSignature:

    @pytest.mark.parametrize('url, string_to_sign, expected_signature', [
        ("http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&Operation=ItemLookup&ItemId=0679722769&ResponseGroup=Images,ItemAttributes,Offers,Reviews&Version=2013-08-01&Timestamp=2014-08-18T12:00:00Z", "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=Images%2CItemAttributes%2COffers%2CReviews&Service=AWSECommerceService&Timestamp=2014-08-18T12%3A00%3A00Z&Version=2013-08-01", "j7bZM0LXZ9eXeZruTqWm2DIvDYVUU3wxPPpp%2BiXxzQc%3D"),
        ("http://webservices.amazon.co.uk/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Operation=ItemSearch&Actor=Johnny%20Depp&ResponseGroup=ItemAttributes,Offers,Images,Reviews,Variations&Version=2013-08-01&SearchIndex=DVD&Sort=salesrank&AssociateTag=mytag-20&Timestamp=2014-08-18T17:34:34.000Z", "GET\nwebservices.amazon.co.uk\n/onca/xml\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Actor=Johnny%20Depp&AssociateTag=mytag-20&Operation=ItemSearch&Operation=ItemSearch&ResponseGroup=ItemAttributes%2COffers%2CImages%2CReviews%2CVariations&SearchIndex=DVD&Service=AWSECommerceService&Sort=salesrank&Timestamp=2014-08-18T17%3A34%3A34.000Z&Version=2013-08-01", "Gv4kWyAAD3xgSGI86I4qZ1zIjAhZYs2H7CRTpeHLD1o%3D"),
        ("http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Operation=CartCreate&Version=2013-08-01&Item.1.OfferListingId=j8ejq9wxDfSYWf2OCp6XQGDsVrWhl08GSQ9m5j%2Be8MS449BN1XGUC3DfU5Zw4nt%2FFBt87cspLow1QXzfvZpvzg%3D%3D&Item.1.Quantity=3&AssociateTag=mytag-20&Timestamp=2014-08-18T17:36:55.000Z", "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&Item.1.OfferListingId=j8ejq9wxDfSYWf2OCp6XQGDsVrWhl08GSQ9m5j%2Be8MS449BN1XGUC3DfU5Zw4nt%2FFBt87cspLow1QXzfvZpvzg%3D%3D&Item.1.Quantity=3&Operation=CartCreate&Operation=ItemSearch&Service=AWSECommerceService&Timestamp=2014-08-18T17%3A36%3A55.000Z&Version=2013-08-01", "LpEUnc9tT4WGneeUwH0LvwxLLfbMEXgmjGX5GXQ1MEQ%3D"),
        ("http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Operation=BrowseNodeLookup&Version=2013-08-01&BrowseNodeId=465600&AssociateTag=mytag-20&ResponseGroup=BrowseNodeInfo,TopSellers,NewReleases,MostWishedFor,MostGifted&Timestamp=2014-08-18T17:38:12.000Z", "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&BrowseNodeId=465600&Operation=BrowseNodeLookup&Operation=ItemSearch&ResponseGroup=BrowseNodeInfo%2CTopSellers%2CNewReleases%2CMostWishedFor%2CMostGifted&Service=AWSECommerceService&Timestamp=2014-08-18T17%3A38%3A12.000Z&Version=2013-08-01", "t48XyuQKLcYROCm7w%2FNqo3mihqB%2FQF2B9b9SX3FIOnU%3D"),
        ("http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Operation=SimilarityLookup&ItemId=B0011ZK6PC,B000NK8EWI&Version=2013-08-01&AssociateTag=mytag-20&ResponseGroup=Offers,ItemAttributes&SimilarityType=Intersection&Condition=New&Merchant=Amazon&Timestamp=2014-08-18T17:39:22.000Z",
        "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&AssociateTag=mytag-20&Condition=New&ItemId=B0011ZK6PC%2CB000NK8EWI&Merchant=Amazon&Operation=ItemSearch&Operation=SimilarityLookup&ResponseGroup=Offers%2CItemAttributes&Service=AWSECommerceService&SimilarityType=Intersection&Timestamp=2014-08-18T17%3A39%3A22.000Z&Version=2013-08-01", "nIlF7C6O1T3faoXIZgGVxYXd%2BD%2F39%2BFPSnwdfiQvy9g%3D")
    ])
    def test_sign_request(self, url, string_to_sign, expected_signature):
      signature = generate_signature(url)
      assert signature == expected_signature