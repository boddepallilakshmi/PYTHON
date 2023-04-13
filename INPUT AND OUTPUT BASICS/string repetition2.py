word = input()
last_three_letters = int(input())
length = len(word)
sliced_length = length - 3
result = word[sliced_length:]
print(result*last_three_letters)
