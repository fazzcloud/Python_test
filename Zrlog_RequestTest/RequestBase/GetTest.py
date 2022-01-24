'''
发送一个get请求，并通过get请求来验证用户是否可以成功获取Zrlog系统服务端的资源
'''
import requests
#定义访问地址
myurl = 'http://106.14.135.177/admin/login'
#通过request库发送get请求
r = requests.get(myurl) #这里是将网页整体返回
#以文本的方式返回响应内容
print(r.text)
#返回协议状态码
print(r.status_code)