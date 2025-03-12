'''' 
To Find the Second largest number, taken a list of numbers to validate
created a function called validation() which iterates each value of list and compares with max variable.
max variable initially set to 0, then first iteration then iterated value will occupy it then on further iteration 
it will compare with next iteration and at the end it max will have height number.

To Make this work across all the list values, the validation function will be invoked by the for loop
which iterates by the range (no of elements) in the list

As each iteration get the max value that value is removed from the list and get added to the sort_list
by this the range - for loop will be jeep reducing till the last value

finally we can get the second value by indexing the sort_list with 1.

Input can be from user input
'''

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