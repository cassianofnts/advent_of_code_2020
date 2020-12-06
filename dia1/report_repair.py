def parte1(input):
    for num1 in input:
        count = input.index(num1)
        for num2 in range(count + 1 , len(input)):
            soma = int(num1) + int(input[num2])
            if soma == 2020:
                return int(num1) * int(input[num2])


def parte2(input):
    for num1 in input:
        count = input.index(num1)
        for num2 in range(count + 1 , len(input)):
            soma = int(num1) + int(input[num2])
            resto = 2020 - soma
            if str(resto) in input:
                return int(num1) * int(input[num2]) * resto

def main():
    with open('input.txt') as arq:
        input = arq.read().splitlines()
    
    mult_parte1 = parte1(input)
    mult_parte2 = parte2(input)

    print(mult_parte1)
    print(mult_parte2)

if __name__ == "__main__":
    main()