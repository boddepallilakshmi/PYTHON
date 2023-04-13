a = int(input())
b = int(input())

equal_to = (a==6) or (b==6)
sum_of_digits = (a+b) == 6
difference = ((a-b) == 6) or ((b-a) == 6)

if equal_to or sum_of_digits or difference:
    print("Lucky")
else:
    print("Not Lucky")
    
