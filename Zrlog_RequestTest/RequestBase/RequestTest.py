import requests
myurl = 'http://106.14.135.177/api/admin/login'
json = {"userName":"admin","password":"6af00c4f834069377b27942531c9ac59","https":False,"key":1643075033935}
header = {'Content-Type': 'application/json'}
#request方法既可以发送post请求，也可以发送get请求
method = 'post'
r = requests.request(url=myurl,json = json,headers = header,method = method)
print(r.text)
print(r.json())