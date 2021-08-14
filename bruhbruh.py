i=0
j=0
num=int(input("enter your number:"))
a=num
b=num
while a>0:
    i=i+(a%10)
    a=int(a/100)
while b>0:
    b=int(b/10)
    j=j+(b%10)
    b=int(b/10)
if (i-j)%11==0:
    print("%d is a multiple of 11"%num)
else:
    print("%d is NOT a multiple of 11"%num)