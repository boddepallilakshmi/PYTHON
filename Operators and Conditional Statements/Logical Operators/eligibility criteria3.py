m = int(input())
p = int(input())
c = int(input())

subject_wise = (m >= 60) and (p >= 50) and (c >= 45)
all_subjects = ((m+p+c) >= 180)

first_condition = subject_wise and all_subjects

total_mp = ((m+p) >=120)
total_cp = ((c+p >= 110))

second_condition = total_mp or total_cp

if first_condition or second_condition:
    print("True")
else:
    print("False")
