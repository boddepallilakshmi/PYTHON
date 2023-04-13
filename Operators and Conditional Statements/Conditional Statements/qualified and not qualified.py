maths=int(input())
physics=int(input())
k=(maths>35) and ((physics)>35)
j=((maths+physics)>=100)
o=(k or j)
if o:
    print("Qualified")
else:
    print("Not Qualified")
