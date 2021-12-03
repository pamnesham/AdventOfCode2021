def calc_position(horizontal, depth):
    position = horizontal * depth
    return position

def calc_aim(direction, new_value, current_aim):
    if direction == "up":
        new_aim = current_aim - new_value
        return new_aim
    else: # direction = down
        new_aim = current_aim + new_value
        return new_aim

def calc_horizontal_and_depth(new_value, current_horizontal, current_aim, current_depth):
    new_horizontal = current_horizontal + new_value
    new_depth = current_depth + (new_value * current_aim)
    return (new_horizontal, new_depth)


def main():
    with open("d2Input.txt") as f:
        directions = f.readlines()

    horizontal = 0
    depth = 0
    aim = 0

    for val in directions:
        val=val.split(" ")
        if val[0]=="forward":
            new_h = calc_horizontal_and_depth(int(val[1]), horizontal, aim, depth)
            horizontal = new_h[0]
            depth = new_h[1]
        else:
            new_a = calc_aim(val[0], int(val[1]), aim)
            aim = new_a
    
    position = calc_position(horizontal, depth)
    print(position)



if __name__=="__main__":
    main()