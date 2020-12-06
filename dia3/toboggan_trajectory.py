from itertools import islice

def quantidade_arvores(input, slope):
    coluna = 0
    contador = 0 
    passo = slope[1]
    
    for linha in islice(input, passo, None, passo): #islice (objeto_a_ser_iterado, 'indice_que_comeca', 'onde parar', 'step')
        
        coluna += slope[0]
        tamanho_da_linha = len(linha) - 1
        
        if coluna > tamanho_da_linha - 1:
            coluna = coluna - tamanho_da_linha  - 1

        if linha[coluna] == '#':
            contador += 1


    return contador
        

def main():

    with open('input.txt', 'r') as arquivo:
        input = arquivo.read().splitlines() 
            
    total_parte_2 = 1

    slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]

    for slope in slopes:
        total_parte_2 *= quantidade_arvores(input, slope)

    total_parte_1 = quantidade_arvores(input, [3,1])

    print(f'Parte 1: {total_parte_1}')
    print(f'Parte 2: {total_parte_2}')

if __name__ == "__main__":
    main()