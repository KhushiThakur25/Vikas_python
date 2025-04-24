'''
print("""world
      gvdeshf
      jhbdjksedjdc""")
a = 57
b = 4

print("Sum of a and b is",a+b)
print("Sum of",a,"and",b,"is",a+b)

#.format string
print("Sum of {} and {} is {}".format(a,b,a+b))
print("Sum of %d and %d is %f"%(a,b,a/b))

print(f"Sum of {a} and {b} is {a+b}")
'''

'''
p = int(input("Enter your physics marks"))
c = int(input("Enter your chemistry marks"))
m = int(input("Enter your maths marks"))
b = int(input("Enter your biology marks"))
co = int(input("Enter your computer marks"))
total = p+c+m+b+co
per = total/5
print(f"Your percentage is {per}")
if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
elif per >= 50:
    print("Grade E")
elif per >= 40:
    print("Grade F")
else:
    print("Fail")


'''

BS = int(input("Enter your basic salary.."))
if BS <= 10000:
    HRA = 0.20 * BS
    DA = 0.80 * BS
elif BS <= 20000:
    HRA = 0.25 * BS
    DA = 0.90 * BS
else:
    HRA = 0.30 * BS
    DA = 0.95 * BS

gross_salary = BS + HRA + DA
print("Your gross salary is:",gross_salary)













