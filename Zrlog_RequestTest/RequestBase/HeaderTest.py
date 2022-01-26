import requests
myurl = 'http://106.14.135.177/api/admin/login'
json = {"userName":"admin","password":"6af00c4f834069377b27942531c9ac59","https":False,"key":1643075033935}
header = {'Content-Type': 'application/json'}
r = requests.post(myurl,json = json,headers =header)
print(r.text)
print(r.json())