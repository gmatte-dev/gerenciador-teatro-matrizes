# Cada fileira tem 12 lugares
# Há 10 fileiras no total = matriz 10x12
# 0 = lugar livre
# 1 = lugar ocupado

#Exercício de matriz e funções: teatro do Cetec (03 e 06/11/2025)
def exibe(mat):

    for fileira in range (10):
        for assento in range (12):
            print(mat[fileira][assento], end=' ')
        print()  

def reserva(mat):

    exibe(mat)

    fileira = int(input("Digite o número da fileira (0-9): "))
    assento = int(input("Digite o número do assento (0-11): "))
    if mat [fileira][assento] == 0 : 
        mat [ fileira ] [ assento ] = 1
        print("Lugar reservado!")
    else: 
        print("Este lugar já está ocupado! ")

    exibe(mat)
    return mat


def libera(mat):

    f = int(input("Informe fileira:"))
    a = int(input("Informe assento:"))

    if mat[f][a] == 1: 
        mat[f][a] = 0 
        print ("Lugar liberado! ")
    else:
        print("Este lugar não está ocupado! ")
    
    return mat


def conta_ocupados_livres(mat):

    livre = 0 
    ocupado = 0
    for i in range (10): 
        for j in range (12): 
            if mat[i][j] == 0: 
                livre += 1 
            else: 
                ocupado += 1 
    print(f"Assentos livres: {livre}")
    print(f"Assentos ocupados: {ocupado}")

def mais_ocupada(mat):
    ocupados_vet = [0] * 10

    for i in range(10):
        cont_ocupados = 0
        for j in range(12):
            if mat[i][j] == 1:
                cont_ocupados += 1
        ocupados_vet[i] = cont_ocupados

    maior = ocupados_vet[0]
    for i in range(1, 10):
        if ocupados_vet[i] > maior:
            maior = ocupados_vet[i]

    print("Fileira(s) com MAIS assentos ocupados:")
    for i in range(10):
        if ocupados_vet[i] == maior:
            print(f"Fileira {i}")
    


def menos_ocupada(mat):

    menosocupados_vet = [0] * 10

    for i in range(10):
        cont_menosocupados = 0
        for j in range(12):
            if mat[i][j] == 1:
                cont_menosocupados += 1
        menosocupados_vet[i] = cont_menosocupados

    menor = menosocupados_vet[0]
    for i in range(1, 10):
        if menosocupados_vet[i] > menor:
            menor = menosocupados_vet[i]

    print("Fileira(s) com MENOS assentos ocupados:")
    for i in range(10):
        if menosocupados_vet[i] == menor:
            print(f"Fileira {i}")
 


def dois_livres(mat):

    f = int(input("Informe o número da fileira: "))

    sim = False 
    for i in range(11):
        if mat[f][i] == 0 and mat[f][i+1] == 0 : 
            print(f"Há dois assentos livres na fileira {f}")
            print (f"Assentos: {i} , {i+1}")
            sim = True 
    if sim == False:  
        print(f"Não há dois lugares lado a lado livres na fileira {f}")


def gravar_arquivo(mat, nome_arquivo):
    arq = open(nome_arquivo, "w")
    
    
    for i in range(10):
        for j in range(12):
            arq.write(str(mat[i][j]) + " ")
        arq.write("\n") 
    arq.close()
    print(f"Matriz registrada no arquivo: {nome_arquivo} ")


def ler_arquivo(nome_arquivo):
    mat = []
    arq = open(nome_arquivo, "r")

    for linha in arq:
        valores = linha.split()  
        linha_convertida = [int(x) for x in valores]  
        mat.append(linha_convertida)

    arq.close() 
    print(f"Arquivo {nome_arquivo} lido")
    return mat



def matriz():
    
    teatro = [[0]*12 for _ in range(10)]

    return teatro 

teatro = matriz ( )

while True:
        print("\n MENU ")
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
            print("Opção inválida. Tente novamente.")
