letter_one = input()
letter_two = input()

first_three_letters_one = letter_one[:3]
first_three_letters_two = letter_two[:3]

result = (first_three_letters_one == first_three_letters_two)

if result:
    print("True")
else:
    print("False")
