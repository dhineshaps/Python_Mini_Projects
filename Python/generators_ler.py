def square_numbers(nums):
    results = []
    for i in nums:
        results.append(i*i)

    return results

#generator_Way
def square_numbers_gen(nums):
    for i in nums:
        print(i)
        yield (i * i)  #generators don't hold entire result in memory , it yield one result a time so it ask for next
        #next is give using 'next' key word



#print(square_numbers([1,3,5]))

my_nums = square_numbers_gen([1,3,5])

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

#print(my_nums)  # <generator object square_numbers_gen at 0x000002AD5000A4D0>

for num in my_nums:  #a way to handle so the next keyword  not need to be used and avaoid failing if no more value to iterate
    print(num)


my_new_nums = ( x*x  for x in [1,6,9])  #other way more similar to list comprehension but with ()

print(list(my_new_nums)) #by using list , values get printed

#generators are better for performance as it not holding memories, if there are millions of records then better to sue genrators


