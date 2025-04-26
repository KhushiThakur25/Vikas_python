Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
age = 20
invite = True
if age > 18:
    print("Welcome to gate 1..")
    if invite:
        print("Welcome to Party..")
    else:
        print("Exit")
else:
    print("You are not eligible.")

Welcome to gate 1..
Welcome to Party..
age = 53
invite = False
if age > 18:
    print("Welcome to gate 1..")
    if invite:
        print("Welcome to Party..")
    else:
        print("Exit")
else:
    print("You are not eligible.")

    
Welcome to gate 1..
Exit
for i in range(0,10,1):
    print("Amit",i)

Amit 0
Amit 1
Amit 2
Amit 3
Amit 4
Amit 5
Amit 6
Amit 7
Amit 8
Amit 9
for i in range(10):
    print("Amit",i)

Amit 0
Amit 1
Amit 2
Amit 3
Amit 4
Amit 5
Amit 6
Amit 7
Amit 8
Amit 9
for i in range(1,11,1):
    print("Amit",i)

Amit 1
Amit 2
Amit 3
Amit 4
Amit 5
Amit 6
Amit 7
Amit 8
Amit 9
Amit 10
for i in range(10,1,-1):
    print("Amit",i)

Amit 10
Amit 9
Amit 8
Amit 7
Amit 6
Amit 5
Amit 4
Amit 3
Amit 2
sum_ = 0
for i in range(1,6):
    sum_ = sum_ + i

sum
<built-in function sum>
sum_
15
sum_ = 0
for i in range(1,6):
    sum_ += i

sum_
15
n = 2
for i in range(2,20):
    print("n = n*i")

n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = 2
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18
2 X 10 = 20
for i in range(2,20):
    print(f"n = n*i")

n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
n = n*i
for i in range(2,20):
    print(f"{n} = {n*i}")

2 = 4
2 = 6
2 = 8
2 = 10
2 = 12
2 = 14
2 = 16
2 = 18
2 = 20
2 = 22
2 = 24
2 = 26
2 = 28
2 = 30
2 = 32
2 = 34
2 = 36
2 = 38
fact = 1
for i in range(6):
    fact *= i

fact
0
fact = 1
for i in range(1,6):
    fact *= i

fact
120
n = 7
for i in range(2,n):
    if n%i == 0:
        print("not prime")
    else:
        print("prime")

prime
prime
prime
prime
prime
prime = True
for i in range(2,n):
    if n%i == 0:
        print("not prime")
        prime = False
        break
if prime:
    print("prime")

SyntaxError: invalid syntax
for i in range(2,n):
    if n%i == 0:
        print("not prime")
        prime = False
...         break
... 
>>> if prime:
...     print("prime")
... 
prime
>>> =============================================
SyntaxError: invalid syntax
>>> n = 7
>>> for i in range(2,n):
...     if n%i == 0:
...         prime = False
...         break
... 
>>> if prime:
...     print("Prime")
... else:
...     print("Not prime")
... 
Prime
