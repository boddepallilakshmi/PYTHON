m = int(input())
p = int(input())
c = int(input())

first_condition = (m >= 70) and (p >= 60) and (c >= 60)
second_condition = ((m + p + c) >= 180)

if first_condition or second_condition:
    print("True")
else:
    print("False")
