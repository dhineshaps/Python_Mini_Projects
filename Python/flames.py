print("Hi Welcome to FLAMES Project")

# name1 = list(input('Please Enter the 1st Person Name: ').lower())
# name2 = list(input('Please Enter the 2nd Person Name: ').lower())

name1 = list("dhine")
name2 = list("dlopd")

# name3 = list("dhine")
# name4 = list("dlopd")
for word1 in name1:
    for word2 in name2:     
       if(word1) == (word2):
          name1.remove(word1)
          name2.remove(word2)
          break


print(len(name1))
print(len(name2))

fnum = len(name1)+len(name2)
print(fnum)

fls = list("flames")

counts = 0

while True:
    for i in fls:
         counts = counts + 1
         if(counts == fnum):
            print("breaking")
            break
    break        
            













        # if(len(fls) == 1):
        #     print("here in breaking")
        #     break
        # elif(count == fnum):
        #     print("removing")
        #     fls.remove(i)
        #     count = 0
        # else:
        #     print("here in incremneting")
        #     count = count + 1