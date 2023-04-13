a = int(input())
b = int(input())
c = int(input())

is_a_greater = a>b and a>c 
if is_a_greater:
    print(a)
else:
    if b>a and b>c:
        print(b)
    else:
        print(c)
