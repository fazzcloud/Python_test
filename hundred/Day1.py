#一行代码实现1-100奇数求和（至少5种方案）
#方案1
res = 0
for i in range(1,100):
    if i % 2 == 1:
        res = res + i
print(res)

#2
sum2 = 0
for i in range(1,100,2):
    sum2 = sum2 + i
print(sum2)

#3
sum3 = sum([i for i in range(1,100) if i%2 == 1])
sum4 = sum([i for i in range(1,100,2)])
sum5 = sum(list(range(1,100))[::2])
print(sum3,sum4,sum5)

