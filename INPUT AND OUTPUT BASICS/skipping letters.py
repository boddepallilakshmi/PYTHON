word  = input()
number = int(input())

result = word[:number] + word[number+1 : ]

print(result)
