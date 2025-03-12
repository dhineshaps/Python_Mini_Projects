'''
To Design a FLAMES Game.
Get the two individual names in two variables, to strike out the common character in both the
the names, iterate outer each other with for loop and inner for loop by this way the common characters
will be strike out and we will get the total number of characters between two variables using the length.

Now the total number of characters between two variables, needs to be iterate over the 'FLAMES' to get the final output,
While loop is created to loop it over until it has only one character left out in flames then break it.

While iterating has initialized the count value as 0, if the for loop reaches the required number which we got
striking out, then remove the FLAMES Character one by one.
'''

print("Hi Welcome to FLAMES Project")

name1 = list(input('Please Enter the 1st Person Name: ').lower())
name2 = list(input('Please Enter the 2nd Person Name: ').lower())

for word1 in name1:
    for word2 in name2:     
       if(word1) == (word2):
          name1.remove(word1)
          name2.remove(word2)
          break

fnum = len(name1)+len(name2)
fls = list("flames")
def validation():
    count = 0
    while True:
        for i in fls:
            if(len(fls)==1):
                return
            elif(count == fnum):
                fls.remove(i)
            else:
                count = count + 1
validation()
print(fls)





