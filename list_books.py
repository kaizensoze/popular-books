
import os
import popbooks.util as util
import requests
import xml.etree.ElementTree as ET

url = "http://webservices.amazon.com/onca/xml?Service=AWSECommerceService&Operation=ItemSearch&SearchIndex=Books&Power=pubdate:after%201500&ResponseGroup=Medium&Sort=salesrank"
url = util.fill_in_url(url)
r = requests.get(url)

# write formatted xml to file
with open('out.xml', 'w') as out:
    out.write(r.text)
# call(['xmllint', '--format', 'out.xml', '>', 'out2.xml'])
os.system('xmllint --format out.xml > out2.xml && mv out2.xml out.xml')

namespaces = {'default': 'http://webservices.amazon.com/AWSECommerceService/2011-08-01'}
root = ET.fromstring(r.content)
items = root.findall('.//default:Item', namespaces)
for item in items:
    attributes = item.find('default:ItemAttributes', namespaces)
    author = attributes.find('default:Author', namespaces).text
    title = attributes.find('default:Title', namespaces).text
    strToPrint = ', '.join([title, author])
    print(strToPrint)