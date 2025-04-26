'''
n = int(input("Enter the term of your series."))
f = 0
s = 1
t = 0
print(f,s,end=" ")
for i in range(n-2):
    t = f + s
    print(t,end = " ")
    f = s
    s = t

'''
'''
n = int(input("Enter the number.."))
i = 1

while i <= 10:
    print(f"{n} X {i} = {n*i}")
    i += 1
'''
'''
n = 525263112
count = 0
while n > 0:
    count += 1
    n //= 10
print(count)
'''

'''
n = 1221
org = n
rev = 0
while n > 0:
    rev = rev*10 + n%10
    n //= 10
print(rev)

#palindrome a = 121,rev = 121

if org == rev:
    print("Palindrome")
else:
    print("Not palindrome")
'''
n = int(input("Enter the value.."))
org = n
count = 0
sum_ = 0
while n > 0:
    count += 1
    n //= 10
print("your count is",count)

n = org
while n > 0:
    sum_ += pow(n%10,count)
    n //= 10
print("your sum is this..",sum_)

if org == sum_:
    print("Number is Armstrong..")
else:
    print("Number is not Armstrong..")








































