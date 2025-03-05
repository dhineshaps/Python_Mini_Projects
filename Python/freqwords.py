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
