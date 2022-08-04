fname=open("dict1.txt")
frd = fname.read()
new_dick = dict()

word = frd.split()

for words in word:
    new_dick[words] = new_dick.get(words,0) + 1

print(new_dick)

bigword= None
bigcount= None

for words,count in new_dick.items():
    if bigcount is None or count > bigcount:
        
        bigcount = count
        bigword = words


    
print(bigword,bigcount)