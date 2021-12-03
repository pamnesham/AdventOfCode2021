def get_bit_counts(bits):
    ones = [0,0,0,0,0,0,0,0,0,0,0,0]
    zeroes = [0,0,0,0,0,0,0,0,0,0,0,0]
    for val in bits:
        for i,bit in enumerate(val):
            if bit=="1":
                ones[i]+=1
            else:
                zeroes[i]+=1
    bit_dict={"ones": ones, "zeroes": zeroes}
    return bit_dict


def get_lead_bit_O(bit_counts, index):
    if bit_counts["ones"][index] > bit_counts["zeroes"][index]:
        lead_bit = 1
    elif bit_counts["ones"][index] < bit_counts["zeroes"][index]:
        lead_bit = 0
    else:
        lead_bit = 2 # if equal
    return lead_bit


def get_lead_bit_c02(bit_counts, index): 
    if bit_counts["ones"][index] > bit_counts["zeroes"][index]:
        lead_bit = 0
    elif bit_counts["ones"][index] < bit_counts["zeroes"][index]:
        lead_bit = 1
    else:
        lead_bit = 2 # if equal
    return lead_bit


def get_list_w_lead_bit(bits, lead_bit, chem, index): 
    list_w_lead_bit = []
    for val in bits:
        if int(val[index]) == lead_bit:
            list_w_lead_bit.append(val)
        elif lead_bit == 2 and chem == "o":
            if int(val[index]) == 1:
                list_w_lead_bit.append(val)
        elif lead_bit == 2 and chem == "c":
            if int(val[index]) == 0:
                list_w_lead_bit.append(val)
    return list_w_lead_bit


def convert_to_decimal(binary):
    total=0
    for ix, b in enumerate(binary):
        converter = int(b)*pow(2,(len(binary)-1-ix))
        total=total+converter
    return(total)


def main():
    with open("input.txt") as f:
        bits = [bit.strip() for bit in f.readlines()]
    o_bits = bits
    
    # Get oxygen generator rating
    index = 0
    while len(o_bits) > 1:
        bit_counts = get_bit_counts(o_bits) #tally 1s and 0s
        lead_bit = get_lead_bit_O(bit_counts, index) # are there more 1s or 0s?
        o_bits = get_list_w_lead_bit(o_bits, lead_bit, "o", index) # create new list with only values starting with either 1 or 0s
        index+=1

    # Get CO2 scrubber rating
    index = 0
    while len(bits) > 1:
        bit_counts = get_bit_counts(bits) #tally 1s and 0s
        lead_bit = get_lead_bit_c02(bit_counts, index) # are there more 1s or 0s?
        bits = get_list_w_lead_bit(bits, lead_bit, "c", index) # create new list with only values starting with either 1 or 0s      
        index+=1  

    oxy_gen = convert_to_decimal(o_bits[0])
    c02_scrub = convert_to_decimal(bits[0])
    life_support = oxy_gen * c02_scrub
    print(life_support)

if __name__=="__main__":
    main()


