'''
To Find the Tallest Student height.

Sample student list is taken in dictionary.

Initial max_height is declared as 0 in variable, dict is now iterated and the student height is
compared with max_height and if it's higher than it will replace the max_height, by this max height will be found.

To get the name of the student/students if more than one student have same height, the height is passed
as a argument to iteration, which gives the list of student/students for the height.

if there are more than one student then response will be in plural or it will be singular.

'''
max_height = 0

stud_height=[]

stud_list = {"Olive":178,"Steve":186,"jose":156,"clive":170,"phil":186}

for name,height in stud_list.items():
    if(height>max_height):
         max_height=height

def get_key_from_value(stud_list, height_value):
    return [key for key, value in stud_list.items() if value == height_value]


name_list = get_key_from_value(stud_list,max_height)

names = len(name_list) - 1

response = ''
for it, s in enumerate(name_list): 
    if(it < names):
      response += s + ", "
    elif(it == names):
      response += s  


print(max_height)
print("Student(s)", response,"is(are) having the same height", max_height)