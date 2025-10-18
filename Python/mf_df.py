import pandas as pd
from collections import defaultdict


col_list = []
funds_by_amc = defaultdict(list)
with open("mf_data.txt") as f:
    for x in f:
         if "Mutual Fund" in x:
            col_list.append(x)

         if ';' in x and 'Scheme Code' not in x:
            schme = x.split(";")[3].strip()
            house = schme.split(" ")[0]
            funds_by_amc[house].append(schme)
         print(funds_by_amc)
         funds_by_amc_new = defaultdict(list)
         for j in col_list:
             print("here")
             print(j)
             for i in funds_by_amc.keys():
                 print(i)
                 new_val =j.split(" ")[0]
                 if new_val == "Jio":
                     new_val = "JioBlackRock"
                 if new_val == "PPFAS":
                     new_val = "Parag"
                 if new_val == "Capitalmind":
                     new_val ="CAPITALMIND"
                 if new_val == "Angel":
                     new_val ="ANGEL"
                 if new_val == "Trust":
                     new_val ="TRUSTMF"
                     print(new_val)
                 if i == new_val:
                    print("foun")
                    for li in funds_by_amc.get(i):
                        funds_by_amc_new[j].append(li)

    


print(col_list)

print(funds_by_amc)
              
     




