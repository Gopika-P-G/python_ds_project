# /bin/bash
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
fname = "testeditor.txt"
fh = open(fname)
count = 0
pam=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        # line = line.rstrip()
        # count = count +1
        continue
    print(line)
    print(float(count))
        
    x=float(line.split()[-1].rstrip())
    count += 1
    pam = pam + x
    print(f"x:{x}, pam: {pam}")
        
print("Average spam confidence:", float(pam)/float(count))
















