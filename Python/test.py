
# my_list = [5, 2, 5, 8, 1]
# def compare_first_with_rest(data_list):
#     if not data_list:
#         return "List is empty"
    
#     first_item = data_list[0]
#     results = []
    
#     for item in data_list[1:]:
#         if item == first_item:
#             results.append(f"{item} is equal to {first_item}")
#         elif item < first_item:
#             results.append(f"{item} is less than {first_item}")
#         else:
#             results.append(f"{item} is greater than {first_item}")
#             my_list.remove(item)
#             results.append(item)
#     return results

# # Example usage:
# #my_list = [5, 2, 5, 8, 1]
# comparison_results = compare_first_with_rest(my_list)

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