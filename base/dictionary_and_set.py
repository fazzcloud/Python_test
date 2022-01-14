#dict
names = {'Michel':95,'bob':75,'tracy':85}
names['Michel'] = 100
names['Michel'] = 0
print(names)
print("Michel"in names)
print(names.get('Michel')) #返回key的索引
print(names.get('Michel11111')) #若key不存在，则返回None
print(names.get('Michel11111',-1)) #若key不存在，也可以指定返回的值
names.pop('Michel')
print(names)

#set
s = set([1,1,2,2,3,3])
print(s)
s.add('lj')
print(s)
s.remove('lj')
print(s)

#不可变对象
a = ['c','a','b']
a.sort() #对list进行排序
print(a)

b = "abc"
c = b.replace('a','A') #替换指定旧字符串为新字符串
print(c)