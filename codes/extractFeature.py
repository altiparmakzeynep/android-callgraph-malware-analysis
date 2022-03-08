
with open('benignCommons.txt','r') as f:
   data = f.readlines()

with open('commonNew.txt','r') as f2:
   data2 = f2.readlines()

mot = []
for i in range(len(data)):
    mot.append(str(data[i]))

lst = []
for j in range(len(data2)):
    lst.append(str(data2[j]))

array = dict((x, lst.count(x)) for x in set(mot))
print(array.values())
#with open('API_Sequence_Counts.txt','a') as f3:
    #for g in medine.items():
        #print(str(g))
        #f3.write(str(g) + "\n")
