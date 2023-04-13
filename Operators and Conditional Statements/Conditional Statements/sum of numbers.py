num1=int(input())
num2=int(input())
k=(num1<20) or (num2<20)
l=(30<(num1+num2)<50)
j=(k or l)
if j:
    print(num1+num2)
else:
    print(num1)
    print(num2)
