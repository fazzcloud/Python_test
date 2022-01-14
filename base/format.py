print('Hello,%s'%('world'))
print('Hi,%s,you have $%d'%('liujing',100))
print('%2d-%02d'%(3,1))
#%2d的意思是按照数字宽度为2输出，并且右对齐，若数字宽度不足2，则补空格
#%02d的意思与%2d类似，宽度不足时，用0补足
print('%.2f'%3.1415926)
print('%.2f'%3.1)
#%.2f的意思是取两位小数，若浮点数不足两位，则自动补0
num = 1
print('%d'%(num)) #结果为1
print('%2d'%(num))#结果为 1
print('%02d'%(num))#结果为01
print('%-2d'%(num))#结果为（1 ）
print('%.2d'%(num))#结果为01 --输出整形时，最少输出两位，如果不够，则在前面自动补0
print('%.2f'%(num))#结果为1.00 --输出浮点型时，最少带两位小数，如果不够，则在后面自动补0
print('%.2d'%(200))#结果为200 --200足够两位，所以完整输出了200
print('%.2f'%(3.14))#结果为3.14

print('Age:%s Gender:%s'%(5,True))
print('growth rate:%s%%'%7)
print('Hello,{0}的成绩提升了{1:.1f}'.format('小明',3.14))

r = 2.5
s = 3.14 * r ** 2
print(f'The area of a circle with redius {r} is {s:.2f}') #将变量r和变量s直接替换占位符

last = 72
now = 85
up = ((now -last)/last)*100
print('小明今年的成绩，比起去年，提升了%.1f%%'%up)
print('小明今年的成绩，比起去年，提升了{0:.1f}%'.format(up))
print(f'小明今年的成绩，比起去年，提升了{up:.1f}%')