'''
To Find the Frequent Words:

Read the file in a variable and initialized an empty dictionary which holds key as words and value
as number of times, it got repeated.

By Using the for loop, iterated over by line by line.
In each line handled the words to lower and striping it and splitting it by spaces.

Now each word will be checked in the dictionary, if the word is not in the dictionary then it will get
added with value as 1, if the word is already there then it will be incremented.

Finally, it is sorted in decreasing order to get the word which has max value and we got the required output

This can also be done by handling the helping verbs, so it won't be part of it.

'''

f = open("/workspaces/Python_Mini_Projects/Python/paragraph.txt", "r")

freq = dict()

for line in f:
    words = line.strip().lower().split(" ")
    for word in words:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

sorted_dict_values = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict_values)
