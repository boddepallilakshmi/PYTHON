str1=input()
str2=input()
k=(str1[:3]=="DIS")  or (str2[:3]=="DIS")
if k:
    print("Discount")
else:
    print("No Discount")
