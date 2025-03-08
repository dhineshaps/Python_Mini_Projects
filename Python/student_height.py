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