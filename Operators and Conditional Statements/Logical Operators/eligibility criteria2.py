m = int(input())
p = int(input())
c = int(input())

subject_wise = (m >=35) and (p >=35) and (c >=35)
any_two_sujects = (m+p >= 90) or (p+c >= 90) or (c+m >=90)

if subject_wise and any_two_sujects:
    print("True")
else:
    print("False")
    
