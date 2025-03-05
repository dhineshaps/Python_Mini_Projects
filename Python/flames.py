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





