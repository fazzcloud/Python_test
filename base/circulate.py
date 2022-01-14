names = ['M','bob','tracy']
for name in names:
    print(name)

number = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    number = number + x
print(number)

sum = 0
for y in list(range(101)):
    sum = sum + y
print(sum)

o = 0
e = 1
while e < 100:
    o = o + e
    e = e + 2
print(o)

L =  ['Bart', 'Lisa', 'Adam']
for x in L:
    print("Hello,",x,"!")

n = 1
while n <= 100:
    if n > 10:#当n>10，结束循环
        break
    print(n)
    n = n + 1
print("end")

i = 0
while i < 10:
    i= i + 1
    if i % 2 == 0:
        continue
    print(i)
print("end")