# read in input file
with open("d1Input.txt") as f:
    readings = f.readlines()

# create vars to hold increase and decrease counts
iCount = 0
dCount = 0

# increase counts based on readings grouped into 3s
for i,v in enumerate(readings):
    a = int(readings[i-1]) + int(readings[i-2]) + int(readings[i-3])
    b = int(readings[i]) + int(readings[i-1]) + int(readings[i-2])
    # ignore the first readings as that will be out of range when calculating a and b
    if i==0 or i==1 or i==2:
        continue
    elif b > a:
        iCount+=1
    else:
        dCount+=1

print("increases: ", iCount)
print("decreases: ", dCount)
