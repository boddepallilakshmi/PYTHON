word=input() 
num=int(input())
k=(word[:num]!=word[len(word)-num:len(word)])
print(k)
