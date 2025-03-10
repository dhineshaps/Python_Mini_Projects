my_list = [5, 2, 15, 8, 1]
sort_list =[]

def validation():
    max = 0
    for i in my_list:
        if(i>max):
            max=i
    return max

for i in range(len(my_list)):   
    cal = validation()
    sort_list.append(cal)
    my_list.remove(cal)

print(sort_list[1])