import sys

# A entrada "n" representa um número
def num_primos(n):
    contador = 0
    # Se o número for < 2, já não é considerado primo (números 1, 0 e negativos),
    # então retorna falso
    if n > 1:
        # Faço um laço numérico de 1 ao número consultado
        for x in range(1, n + 1):
            # Faço a divisão do número com a saída do laço (x),
            # para verificar se é divisível
            if n % x == 0:
                # Como ele só deve ser dividido por 1 e por ele mesmo,
                # o contador não deve passar de 2, ou não será número primo
                contador += 1
                # Se passar de dois, encerro o laço retornando falso
                if contador == 3:
                    break
        if contador == 2:
            return True
        else:
            return False
    else:
        return False

# Função para tratamento da entrada do numeral
def mostra_primos():
    # A variável numeral recebe o número na forma de string
    numeral = sys.argv[1]
    # Converto para inteiro o numeral
    numeral = int(numeral)
    # Faço o laço indo do número 2 até o número
    # que o usuário colocou na entrada
    for n in range(2, numeral + 1):
        # Chama a função num_primos para verificar quais números são primos
        if num_primos(n):
            print(f"{n} é um número primo")

if __name__ == "__main__":
    mostra_primos()
