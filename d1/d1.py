with open("d1Input.txt") as f:
    readings = f.readlines()

iCount = 0
dCount = 0

for i,v in enumerate(readings):
    v=v.strip()
    a = int(readings[i-1]) + int(readings[i-2]) + int(readings[i-3])
    b = int(readings[i]) + int(readings[i-1]) + int(readings[i-2])
    if i==0 or i==1 or i==2:
        continue
    elif b > a:
        iCount+=1
    else:
        dCount+=1

print("increases: ", iCount)
print("decreases: ", dCount)
