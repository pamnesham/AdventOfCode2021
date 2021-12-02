# calculate the overall position
def calc_position(horizontal, depth):
    position = horizontal * depth
    return position


# calculate aim (aim added in challenge 2)
def calc_aim(direction, x, current_aim):
    if direction == "up":
        new_aim = current_aim - x
        return (0, new_aim)
    elif direction == "down":
        new_aim = current_aim + x
        return (0, new_aim)
    else:
        return "error"


# calculate horizontal 
# challenge 2 has horizontal change affecting depth
def calc_horizontal(x, current_horizontal, current_aim, current_depth):
    new_horizontal = current_horizontal + x
    new_depth = current_depth + (x * current_aim)
    return (new_horizontal, new_depth)


def main():
    # read input values
    with open("d2Input.txt") as f:
        directions = f.readlines()

    # create vars to be calculated
    horizontal = 0
    depth = 0
    aim = 0

    # calculations
    for i,val in enumerate(directions):
        val=val.split(" ")
        if val[0]=="forward":
            new_h = calc_horizontal(int(val[1]), horizontal, aim, depth)
            horizontal = new_h[0]
            depth = new_h[1]
        else:
            new_a = calc_aim(val[0], int(val[1]), aim)
            aim = new_a[1]
    
    position = calc_position(horizontal, depth)
    print(position)



if __name__=="__main__":
    main()