import requests
#获取url
myurl = 'http://106.14.135.177/api/admin/login'
#请求的数据为json串，并将请求的数据保存在data字典中
data = {"userName":"admin","password":"305771d8dc44a7b717c4d8a44eab8f36","https":False,"key":1643017708746}
#通过requests库发送POst请求，其中verify=False代表绕过Https证书验证
r_res = requests.post(url=myurl,json=data,verify=False)
print(r_res.text)
print(r_res.json())
