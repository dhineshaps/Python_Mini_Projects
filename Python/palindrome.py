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