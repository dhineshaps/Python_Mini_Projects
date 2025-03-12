'''
To Find the given word is Palindrome.

Made the given word as list variable and initialized a empty string variable.

Iterated the given word list with range, so that no of times the negative index will 
have the value from the last and it is stored in the initialized empty variable.

finally the  given word and string variable is compared, if both are same then it is palindrome
'''

word="malayalam"
lword = list(word)
palword=""
for i in range(1,len(lword)+1):
    cal=lword[-i]
    palword += cal

if(word == palword):
    print("It is Palindrome")
else:
    print("it is not palindrome")