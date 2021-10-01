#!/usr/local/bin/python3

class cores:

    ERRO = '\033[1;91m'
    NORMAL = '\033[0;0m'
    CERTO = '\033[1;34m'
    PERG = '\033\033[1;32m'


def cria_matriz():  # cria a matriz 3x3 que baseia o jogo
    matriz = []
    for i in range(3):
        linha = []
        for i in range(3):
            linha.append("_")
        matriz.append(linha)
    return matriz  # retorna a matriz 3x3 com todos os elementos '_'


def verifica_par(x):  # verifica se a variável controle é par
    if x % 2 == 0:
        return True
    else:
        return False


def verifica_vitoria(matriz):
    resultado = False
    for i in range(3):  # verifica a sequencia nas linhas
        if matriz[i][0] == matriz[i][1] == matriz[i][2] and matriz[i][0] != '_':
            resultado = True
    for j in range(3):  # verifica a sequencia nas colunas
        if matriz[0][j] == matriz[1][j] == matriz[2][j] and matriz[0][j] != '_':
            resultado = True
    # verifica as diagonais
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != '_':
        resultado = True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != '_':
        resultado = True
    return resultado  # retorna se houve a vitória


def controle_jogo(nome1, nome2):
    user1 = nome1  # nome dos jogadores
    user2 = nome2
    print(cores.PERG+"Lembrete: As coordenadas devem ser os números inteiros 1, 2 ou 3."+cores.NORMAL)
    matriz_final = cria_matriz()  # constroi a matriz base
    for i in matriz_final:  # printa a matriz de modo mais bonito
        print(i)
    controle = 0  # variável para o controle de qual letra deve ser preenchida
    vitoria = False  # controle do laço
    while vitoria == False:
        if verifica_par(controle) == True:  # variável controle é par
            evita_repeticao = False  # evita quebrar o código em caso de posição repetida
            while evita_repeticao == False:
                evita_input_errado = False  # evita quebrar o códifo em caso de input errado
                while evita_input_errado == False:
                    linha = int(
                        input("Qual a linha que %s deseja escolher? " % (user1)))
                    coluna = int(
                        input("Qual a coluna que %s deseja escolher? " % (user1)))
                    linha -= 1 #corrige o input para as coordenadas
                    coluna -= 1
                    if linha >= 3 or linha < 0 or coluna >= 3 or coluna < 0:
                        print(cores.ERRO+'As coordenadas dadas estão erradas! Tente novamente!'+cores.NORMAL)
                    else:
                        evita_input_errado = True
                if matriz_final[linha][coluna] == '_':
                    # substitui a coordenada pela letra
                    matriz_final[linha][coluna] = "X"
                    evita_repeticao = True  # permite o prosseguimento do código
                else:
                    print(cores.ERRO+"Essa posição já foi utilizada! Tente novamente!"+cores.NORMAL)
            for i in matriz_final:
                print(i)  # printa o estado atual
            if verifica_vitoria(matriz_final) == True:
                print(cores.CERTO+"%s venceu!" % (user1)+cores.NORMAL)
                vitoria = True
            else:
                if controle == 8:  # não há mais jogadas disponíveis, decreta Velha
                    print(cores.CERTO+"Deu velha!"+cores.NORMAL)
                    vitoria = True
                else:
                    controle += 1

        else:
            evita_repeticao = False
            while evita_repeticao == False:
                evita_input_errado = False
                while evita_input_errado == False:
                    linha = int(
                        input("Qual a linha que %s deseja escolher? " % (user2)))
                    coluna = int(
                        input("Qual a coluna que %s deseja escolher? " % (user2)))
                    linha -= 1
                    coluna -= 1
                    if linha >= 3 or linha < 0 or coluna >= 3 or coluna < 0:
                        print(cores.ERRO+'As coordenadas dadas estão erradas! Tente novamente!'+cores.NORMAL)
                    else:
                        evita_input_errado = True
                if matriz_final[linha][coluna] == '_':
                    # substitui a coordenada pela letra
                    matriz_final[linha][coluna] = "O"
                    evita_repeticao = True
                else:
                    print(cores.ERRO+"Essa posição já foi utilizada! Tente novamente"+cores.NORMAL)
            for i in matriz_final:
                print(i)
            if verifica_vitoria(matriz_final) == True:
                print(cores.CERTO+"%s venceu!" % (user2)+cores.NORMAL)
                vitoria = True
            else:
                controle += 1


def main():
    user1 = str(input("Qual o nome do jogador 1? (X) "))  # nome dos jogadores
    user2 = str(input("Qual o nome do jogador 2? (O) "))
    controle_jogo(user1, user2)


main()
