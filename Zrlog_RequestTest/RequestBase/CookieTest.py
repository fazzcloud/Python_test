import requests
#获取接口地址
myurl = 'http://106.14.135.177/api/admin/article/create'
#定义请求中各项参数
myjson = {"id":None,
          "editorType":"markdown",
          "title":"测试cookie",
          "alias":"测试cookie",
          "thumbnail":None,
          "typeId":"1",
          "keywords":None,
          "digest":None,
          "canComment":False,"recommended":False,"privacy":False,"content":"<p>你好</p>\n","markdown":"你好","rubbish":False}
myheaders = {'Content-Type': 'application/json'}
mycookies = {'admin-token':'1#7948745359757143547862695462326D536F4136553653463446564F4858455152397550636264655234386B54555542337A394877504278464249524C5A584E7537484A527474506D4A78584B47495149784647755369372B36417A473669444C4474386C7246655233413D'}
#发送post请求
res = requests.post(myurl,json=myjson,headers = myheaders,cookies = mycookies)
#打印返回值
print(res.json())