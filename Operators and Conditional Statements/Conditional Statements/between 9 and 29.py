a = input()
a = int(a)
b = input()
b = int(b)
c = input()
c = int(c)

range_a = a>=10 and a<=20
range_b = b>=10 and b<=20
range_c = c>=10 and c<=20

range_abc = range_a or range_b or range_c
print(range_abc)
