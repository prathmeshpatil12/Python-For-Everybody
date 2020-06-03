import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
print("Retrieving", url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
print("Retrieved", len(data), "characters.")
info = json.loads(data)
info = info['comments']
print("Count: ", len(info) )

#print(json.dumps(info ,indent=4))
sums = 0
for item in info:
    sums = sums + item['count']

print("Count: ", sums)


