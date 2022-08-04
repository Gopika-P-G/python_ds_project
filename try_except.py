fhand = input("Enter the File Name:")

try:
	fhand = open(fhand) 
except:
		print("could not find the file with that name ")
		quit()
inp =fhand.read()
print(len(inp))