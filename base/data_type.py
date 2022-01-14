print('I\'m ok') #用\转义’
print('i\'m learning\npython')#用\转义’，同时用\n换行
print('\\\n\\')#用\\转义\，同时用\n换行
print('''
1
2
3
''')
print(r'\\\n\\')
print(True and True,True and False,5 > 3 and 5 < 3)
print(True or False,False or False,5 > 3 or 5 < 3)
print(not False,not True,not 1 > 2)

age = int(input('How old:'))
if age > 8:
    print('adult')
else:
    print('teenager')

n = 123
f = 456.789
s1 = 'Hello,world!'
s2 = 'Hello,\'Ada\''
s3 = r'Hello,"Brain"'
s4 = r''' Hello,
    Lisa!
'''
print(n,f,s1,s2,s3,s4)