#CONFIGURAÇÕES
FILEIRAS = 10
ASSENTOS = 12
LIVRE = 0
OCUPADO = 1


# FUNÇÕES

def exibe(mat):
    print("\nMapa do teatro (0 = livre | 1 = ocupado)")
    for i in range(FILEIRAS):
        for j in range(ASSENTOS):
            print(mat[i][j], end=" ")
        print()


def reserva(mat):
    exibe(mat)

    fileira = int(input("Digite a fileira (0-9): "))
    assento = int(input("Digite o assento (0-11): "))

    # validação
    if fileira < 0 or fileira >= FILEIRAS or assento < 0 or assento >= ASSENTOS:
        print("Posição inválida!")
        return mat

    if mat[fileira][assento] == LIVRE:
        mat[fileira][assento] = OCUPADO
        print("Lugar reservado!")
    else:
        print("Este lugar já está ocupado!")

    return mat


def libera(mat):
    fileira = int(input("Informe a fileira: "))
    assento = int(input("Informe o assento: "))

    if fileira < 0 or fileira >= FILEIRAS or assento < 0 or assento >= ASSENTOS:
        print("Posição inválida!")
        return mat

    if mat[fileira][assento] == OCUPADO:
        mat[fileira][assento] = LIVRE
        print("Lugar liberado!")
    else:
        print("Este lugar já está livre!")

    return mat


def conta_ocupados_livres(mat):
    livres = 0
    ocupados = 0

    for i in range(FILEIRAS):
        for j in range(ASSENTOS):
            if mat[i][j] == LIVRE:
                livres += 1
            else:
                ocupados += 1

    print("Assentos livres:", livres)
    print("Assentos ocupados:", ocupados)


def mais_ocupada(mat):
    ocupados_vet = [0] * FILEIRAS

    for i in range(FILEIRAS):
        cont = 0
        for j in range(ASSENTOS):
            if mat[i][j] == OCUPADO:
                cont += 1
        ocupados_vet[i] = cont

    maior = ocupados_vet[0]
    for i in range(1, FILEIRAS):
        if ocupados_vet[i] > maior:
            maior = ocupados_vet[i]

    print("Fileira(s) com MAIS lugares ocupados:")
    for i in range(FILEIRAS):
        if ocupados_vet[i] == maior:
            print("Fileira", i)


def menos_ocupada(mat):
    ocupados_vet = [0] * FILEIRAS

    for i in range(FILEIRAS):
        cont = 0
        for j in range(ASSENTOS):
            if mat[i][j] == OCUPADO:
                cont += 1
        ocupados_vet[i] = cont

    menor = ocupados_vet[0]
    for i in range(1, FILEIRAS):
        if ocupados_vet[i] < menor:
            menor = ocupados_vet[i]

    print("Fileira(s) com MENOS lugares ocupados:")
    for i in range(FILEIRAS):
        if ocupados_vet[i] == menor:
            print("Fileira", i)


def dois_livres(mat):
    fileira = int(input("Informe a fileira: "))

    if fileira < 0 or fileira >= FILEIRAS:
        print("Fileira inválida!")
        return

    encontrou = False
    for i in range(ASSENTOS - 1):
        if mat[fileira][i] == LIVRE and mat[fileira][i + 1] == LIVRE:
            print("Dois lugares livres:", i, "e", i + 1)
            encontrou = True

    if encontrou == False:
        print("Não há dois lugares livres lado a lado.")


def gravar_arquivo(mat, nome):
    arq = open(nome, "w")

    for i in range(FILEIRAS):
        for j in range(ASSENTOS):
            arq.write(str(mat[i][j]) + " ")
        arq.write("\n")

    arq.close()
    print("Arquivo gravado com sucesso!")


def ler_arquivo(nome):
    mat = []
    arq = open(nome, "r")

    for linha in arq:
        valores = linha.split()
        linha_convertida = []
        for v in valores:
            linha_convertida.append(int(v))
        mat.append(linha_convertida)

    arq.close()
    print("Arquivo lido com sucesso!")
    return mat


def cria_matriz():
    return [[LIVRE] * ASSENTOS for _ in range(FILEIRAS)]



# PROGRAMA PRINCIPAL

teatro = cria_matriz()

while True:
    print("\nMENU")
    print("1 - Exibir lugares")
    print("2 - Reservar lugar")
    print("3 - Liberar lugar")
    print("4 - Contar lugares")
    print("5 - Fileira mais ocupada")
    print("6 - Fileira menos ocupada")
    print("7 - Verificar dois lugares livres juntos")
    print("8 - Gravar no arquivo")
    print("9 - Ler do arquivo")
    print("0 - Sair")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        exibe(teatro)
    elif opc == "2":
        teatro = reserva(teatro)
    elif opc == "3":
        teatro = libera(teatro)
    elif opc == "4":
        conta_ocupados_livres(teatro)
    elif opc == "5":
        mais_ocupada(teatro)
    elif opc == "6":
        menos_ocupada(teatro)
    elif opc == "7":
        dois_livres(teatro)
    elif opc == "8":
        gravar_arquivo(teatro, "teatro.txt")
    elif opc == "9":
        teatro = ler_arquivo("teatro.txt")
    elif opc == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!")

