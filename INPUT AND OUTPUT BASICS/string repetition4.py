word = input()

length = len(word)

first_two_characters = word[:2]
last_two_characters = word[length-2:]
middle_characters = (length-4) * "*"

print(first_two_characters + middle_characters + last_two_characters)
