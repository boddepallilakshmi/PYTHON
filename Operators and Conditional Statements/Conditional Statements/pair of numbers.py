num1=int(input())
num2=int(input())
a=(num1<=1000) and (num2<=1000)
b=(num2>500)
e=(a or b)
if e:
    print("Pair")
else:
    print("Not a Pair")
