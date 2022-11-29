def main():    
    with open("input1.txt") as f:
        binarios = [line.strip() for line in f]

    gamma = ''
    epsilon = ''
    for column in range(len(binarios[0])):
        um = 0
        zero = 0
        for row in binarios:
            if row[column] == "1":
                um += 1
            else:
                zero += 1
        most, least = ('1', '0') if um > zero else ('0', '1')
        gamma += most
        epsilon += least

    print(int(gamma, 2)*int(epsilon, 2))




if __name__=="__main__":
    main()