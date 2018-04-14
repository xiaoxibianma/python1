# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
total = 0
count =0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(':')
    number= float(line[pos+1:])
    total = total + number
    count = count+1

print("Average spam confidence:",total/count)
