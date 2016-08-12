
import popbooks.util as util

url = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&SearchIndex=Books" # &Sort=review-count-rank|review-rank 
url = util.fill_in_url(url)
print(url)