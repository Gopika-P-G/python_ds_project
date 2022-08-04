text = "X-DSPAM-Confidence:    0.8475"
line = text.find("0")
#print(line)
slicing=text[line: ]
print(float(slicing))