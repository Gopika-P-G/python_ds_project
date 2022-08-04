fhand=open('testeditor.txt')

for line in fhand:
    line =line.lstrip()
    if not line.startswith("I"):   #if line.startswith("I") use you don't use the continue
        continue                   
print(line)