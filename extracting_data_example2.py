fname = input("Enter file name: ")

emailfile=open(fname,'r')

new_dict = {}
hourlist=[]
count = 0
for word  in emailfile.readlines():
    word = word.rstrip()
    #word.split(" ")
    #print("word:", word)

    if word.startswith("From "):
        word_split_list = word.split(" ")
        count+=1
        time=word_split_list[6].split(":")
        hourlist.append(time[0])
print(hourlist)
for hours in hourlist:
    new_dict[hours] = new_dict.get(hours,0) +1
print(new_dict.items()) 

for k,v in sorted(new_dict.items()):
    print(k,v)





