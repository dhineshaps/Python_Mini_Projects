sent = "A guitar has six strings".lower().replace(" ","")

nonrep = dict()

for word in sent:
    if word not in nonrep:
      nonrep[word] = 1
    else:
     nonrep[word] += 1


nonrepchar = ""

for key, value in nonrep.items():
    if(value==1):
        nonrepchar += key
        break


print("The First non repeating character in the given string is ",nonrepchar )