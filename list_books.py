
import popbooks.util as util
import requests

url = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&SearchIndex=Books&Power=pubdate:after%201900" # &Sort=review-count-rank|review-rank 
url = util.fill_in_url(url)
# print(url)
r = requests.get(url)
print(r.text)
