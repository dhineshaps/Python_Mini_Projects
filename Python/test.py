
flam = list("FLAMES")


print(len(flam))

# for i in range(7):
#     print(i)

# for i in flam:
#     print(i)
#     if (i =='L'):
#         break

flamn = list("FLAMES")

#count = 0

def validation():
    count = 0
    while True:
        for i in flam:
            if(len(flamn)==1):
                return
            elif(count == 7):
                flamn.remove(i)
            else:
                count = count + 1



validation()
print(flamn)           

# def validation():
#     while True:
#         for i in flam:
#             print(i)
#             if (i =='L'):
#                  flamn.remove(i)
#                  return

# validation()
# print(flamn)
# while True:
#     for i in flam:
#         if(i == 'L'):
#              continue