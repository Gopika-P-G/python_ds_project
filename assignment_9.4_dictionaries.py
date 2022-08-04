fname = input("Enter file name: ")

emailfile=open(fname,'r')

dictn={}
emaillist=[]
count = 0
for word  in emailfile.readlines():
    word = word.rstrip()
    #word.split(" ")
    #print("word:", word)

    if word.startswith("From "):
		word_split_list = word.split(" ")
		count+=1
		emaillist.append(word_split_list[1])


for emailid in emaillist:
    dictn[emailid]=dictn.get(emailid,0)+1
#print(dictn)
    
bigword = None
bigcount =None
for k,v in dictn.items():
    if bigcount is None or v > bigcount:
		bigcount = v
		bigword = k
print(bigword,bigcount)