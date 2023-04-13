first_line = input()
second_line = input()
length_first_line = len(first_line) - 3
length_second_line = len(second_line) - 3

result = first_line[length_first_line : ] == second_line[length_second_line : ]

print(result)


