word1=input()
word2=input()
num1=int(input()) 

k=(word1[num1:num1+len(word2)]==word2[:])
print(k)
