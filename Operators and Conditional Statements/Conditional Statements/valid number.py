num=int(input())
str1=str(num)
a=str1[0]
b=str1[1]
c=str1[2]
k=(int(a)!=5) or (int(b)!=5) or (int(c)!=5)
l=(300<num<700)
if (k and l):
    print("Valid Number")
else:
    print("Not a Valid Number")
