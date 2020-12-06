def le_linhas(linha):
    
    tokens = linha.rstrip().split(' ')
    num1, num2 = map(int, tokens[0].split('-'))
    letra = tokens[1][0]
    password = tokens[2]
    
    return num1, num2, letra, password


def parte1(linha):
    min, max, letra, password = le_linhas(linha)

    if min <= password.count(letra) <= max:
        return 1
      
    return 0

def parte2(linha):
    primeira_posicao, segunda_posicao, letra, password = le_linhas(linha)

    if (password[primeira_posicao - 1] == letra) != (password[segunda_posicao - 1] == letra):
        return 1

    return 0

def main():

    password_parte1 = 0
    password_parte2 = 0

    with open('input.txt', 'r') as arquivo:
        input = arquivo.read().splitlines() 

    for linha in input:
        password_parte1 += parte1(linha)
        password_parte2 += parte2(linha)

    print('\n\nPassword validas: ')
    print(f'\tParte 1: {password_parte1}')
    print(f'\tParte 2: {password_parte2}\n\n')


if __name__ == "__main__":
    main()