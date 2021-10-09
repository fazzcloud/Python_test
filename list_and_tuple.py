classmate = ['marile','bob','david']
print(len(classmate))
print(classmate[0],classmate[1])
print(classmate[-1],classmate[-2],classmate[-3])
classmate.append('lily') #.append()用于在列表末尾插入元素
classmate.insert(1,'ll') #.insert()用于在列表中指定位置插入元素(索引位置,元素)
print(classmate)
classmate.pop() #默认删除列表末尾的元素
classmate.pop(1)#删除指定索引位置的元素
print(classmate)
classmate[1] = 'lly'
print(classmate)
L = ['liujing',1,8.21,True]
print(L)
classmate[1] = L
print(classmate)
print(L[2])
print(classmate[1][2])
t = ('a','b',L)
print(t)
t[2][1] = 2
t[2][3] = 3.14
print(t)

L2 = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

#Apple
print(L2[0][0])
# 打印Python:
print(L2[1][1])
# 打印Lisa:
print(L2[2][2])