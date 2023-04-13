str1=input()
num=int(input())
a=(str1=="large")
b=(num>=300)
e=(a or b)
if e:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")
