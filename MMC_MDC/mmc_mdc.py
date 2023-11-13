import sys
import os

# Este trecho do código adiciona o diretório pai do diretório atual
# ao caminho de busca do Python e importa a função num_primos do
# arquivo numeros_primos.py que está na pasta Numeros_primos
CAMINHO = f"{os.path.dirname(os.path.abspath(__file__))}"
sys.path.append(f"{CAMINHO}/..")
from Numeros_primos.numeros_primos import num_primos

def pega_primos(num):
    # Cria uma lista para adicionar os números primos necessários
    lista_primos = list()
    # Usa a função max() para obter o maior número de entrada
    # e usá-lo como limite dos números primos necessários
    for p in range(1, max(num) + 1):
        # Usa a função num_primos para receber apenas os números primos
        if num_primos(p):
            lista_primos.append(p)
    return lista_primos

def mmc(num):
    # Envia a lista numérica para a função pega_primos e recebe
    # os números primos necessários para o cálculo
    lista_primos = pega_primos(num)

    # Pequena parte do código para mostrar o cálculo na tela
    entrada = ""
    print('')
    for y in num:
        entrada += str(f"{y}, ")

    entrada = entrada[:-2]
    print(entrada, end=" ")

    # A lista_mm será responsável por armazenar os números primos usados na divisão
    lista_mm = list()
    # A variável cont_list será responsável por controlar o retorno aos
    # números primos menores, caso os maiores não realizem a divisão
    cont_list = 0
    # As variáveis cont_primo e result_mdc serão responsáveis por definir
    # qual é o MDC do cálculo
    cont_primo = 0
    result_mdc = 1
    
    while True:
        # A variável cont_x será responsável pelo controle dos números de entrada, substituindo
        # o valor original pelo resultado da divisão
        cont_x = 0
        # A variável contem será responsável por não repetir o número primo no mesmo loop
        # e ajudar a variável cont_list a controlar os números primos
        # Assim, sempre que o loop passar por aqui, ela será tornada falsa
        contem = False
        for x in num:
            # Se o resto da divisão do número de entrada, representado pela variável x,
            # com o número primo for igual a 0, entra no laço
            if x % lista_primos[cont_list] == 0:
                if not contem:
                    # Pequena parte do código para mostrar o cálculo na tela
                    print(f"| {lista_primos[cont_list]}")
                    # Adiciona o número primo usado na divisão para a lista_mm
                    lista_mm.append(lista_primos[cont_list])
                # A variável cont_primo faz o controle para achar o MDC
                cont_primo += 1
                if cont_primo == len(num):
                    # A variável result_mdc recebe os números primos e realiza os cálculos
                    # para encontrar o MDC 
                    result_mdc *= lista_primos[cont_list]
                    
                # Faz a troca do número original pelo resultado da divisão
                num[cont_x] = int(x / lista_primos[cont_list])
                # Faz a troca da variável False para True, garantindo que não entre mais
                # números primos para a lista_mm, e zera a variável cont_list para voltar
                # aos números primos menores
                contem = True

            cont_x += 1
        cont_primo = 0
        # Verifica se a soma de todos os números de entrada é igual à quantidade
        # dos números introduzidos; se for verdadeiro, termina a execução
        if sum(num) == len(num):
            break
        # Fazendo o controle da variável cont_list
        if contem:
            # Pequena parte do código para mostrar o cálculo na tela
            y = ""
            for x in num:
                y += str(f"{x}, ")
            print(y[:-2], end=" ")

            cont_list = 0
        else:
            cont_list += 1
    # Chama a função multiplica para multiplicar todos os números primos usados na divisão
    # e retorna o resultado para a variável resposta
    result_mmc = multiplica(lista_mm)
    return result_mmc, result_mdc

def multiplica(lista):
    # Realiza a multiplicação de todos os números e retorna o resultado
    resultado = 1
    for mmc in lista:
        resultado *= mmc

    return resultado

def entrada_sys():
    # sys.argv pega a entrada como lista: ex [mmc.py, 60, 110, 126]
    entrada = sys.argv
    # Del para deletar o primeiro elemento da lista [mmc.py]
    # deixando apenas os números
    del entrada[0]
    # O cont será usado para ajudar a transformar os elementos que estão
    # em string para inteiros
    cont = 0
    # Laço para converter as strings para inteiros
    for num in entrada:
        # O replace retira as vírgulas da entrada, caso existam, para evitar erros ao
        # converter a string para inteiro
        num = num.replace(',', '')
        num = int(num)
        entrada[cont] = num
        cont += 1
    # Envia a lista com os números a serem calculados para a função mmc()
    # e ela retornará o resultado dos cálculos
    result_mmc, result_mdc = mmc(entrada)
    print(f"\nO MMC é {result_mmc}")
    print(f"O MDC é {result_mdc}\n")

if __name__ == "__main__":
    entrada_sys()
