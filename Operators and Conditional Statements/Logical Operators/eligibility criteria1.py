m = int(input())
p = int(input())
c = int(input())

any_two_subjects = (m+p >=100) or (p+c >=100) or (c+m >=100)
all_subjects = ((m+p+c) >= 180)

if any_two_subjects and all_subjects:
    print("True")
else:
    print("False")
