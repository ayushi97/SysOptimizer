
import re

with open("ss.txt") as outfile:
    lines = (line.strip() for line in outfile)
    lines = list(line for line in lines if line)

found = False
final = {}
useless = {}

for i  in  lines:
    if(i.split(' ', 1)[0] == 'PID'):
        found = True
        continue
    if(found):
        i = re.sub(' +',' ', i)
        list1  = list(i.split(' '))
        list1[0] =  float(list1[0])
        list1[8] =  float(list1[8])
        list1[9] =  float(list1[9])
        if(list1[8] or list1[9] != 0):
            final[list1[0]] =  [list1[1] ,  list1[8] , list1[9] , list1[11]]
        else:
            useless[list1[0]] =  [list1[1] ,  list1[8] , list1[9] , list1[11]]

print("************ FINAL ********* \n ************************** \n ***********************")
for i in final:
    print(final[i])

print("************ USELESS ********* \n ************ USELESS ********* \n ************ USELESS *********")
for i in useless:
    print(useless[i])
