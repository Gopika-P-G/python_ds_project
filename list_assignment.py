fname = input("Enter file name: ")
fh = open(fname)
inp = fh.read()
duplicate_list=[]
non_duplicate_list=[]

for line in inp:
    line = inp.split()
    line.sort()
#print(line)
for item  in line:
    duplicate_list.append(item)
#print(duplicate_list)

for i in duplicate_list:
    if i not in non_duplicate_list:   
        non_duplicate_list.append(i)
print(non_duplicate_list)    
   
        

        
 
     
    
