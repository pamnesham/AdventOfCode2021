with open("d1Input.txt") as f:
    readings = f.readlines()

# increase counts based on readings grouped into 3s
increase_count = 0
for i,v in enumerate(readings):
    a = int(readings[i-1]) + int(readings[i-2]) + int(readings[i-3])
    b = int(readings[i]) + int(readings[i-1]) + int(readings[i-2])
    if i < 3:  # ignore the first readings as that will be out of range when calculating a and b
        continue
    elif b > a:
        increase_count+=1

print("increases: ", increase_count)
