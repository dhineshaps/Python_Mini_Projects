#list,tules, dict, generators can be looped over


#___iter__() is the dunder menthod which makes the list,tuples, dict etc as iter

list_test = [1,23,2]

print(dir(list_test))  #__iter__

#so in the backend when we use for loop it uses the __iter__ on that object to loop over

for i in list_test:  #uses the __iter__
    print(i)  #iteratable

#iterator is obeject with state

# Iterator itself cant get the next item as there is no dunder method like __next__


i_nums =  iter(list_test) #list_test.__iter__() -> iter(list_test) can be called like this,   
#this is what for loop does in the background



print(i_nums) #<list_iterator object at 0x000001E22A8926B0>
print(dir(i_nums))  #here the iter -> iterator has the __next__

print(next(i_nums))  #here we able to get the output

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break