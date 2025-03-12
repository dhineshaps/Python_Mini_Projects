'''
To Find the non-repeated word in a given string

Assign the required string to the variable by making it as lower case and removing the space, and 
initialize the empty dictionary which going to hold each word as key and number of occurrences as value.

Iterate over each word in the sentence and if the word is not in the dict then add it by assigning the
value as 1, if the word already exits then increment the value by 1

now the dictionary holds the words and no of occurrence.

now iterate over the dictionary and if the value is 1 then stop  as it is the first non-repeating 
word in the sentence

'''

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