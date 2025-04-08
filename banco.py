nome = input("Qual seu nome: ")
totalConta = 0
mensagens = []

def saque():
    global totalConta
    while True:
        saqueValor = float(input("Digite o valor do saque: "))
        if saqueValor <= 0 or saqueValor > totalConta:
            print("Digite um valor válido!")
        else:
            totalConta -= saqueValor
            mensagem = f"{nome.title()} fez um saque. Novo saldo: R${totalConta:.2f}"
            mensagens.append(mensagem)
            print(mensagem)
            break  

def deposito():
    global totalConta
    while True:
        depositoValor = float(input("Digite o valor do depósito: "))
        if depositoValor < 0:
            print("Digite um valor válido!!")
        else:
            totalConta += depositoValor
            mensagem = f"{nome.title()} fez um depósito. Novo saldo: R${totalConta:.2f}"
            mensagens.append(mensagem)
            print(mensagem)
            break  

def extrato():
    print("\n--- Extrato de operações ---")
    if mensagens:
        print("\n".join(mensagens))
    else:
        print("Nenhuma operação realizada ainda.")
    print("-----------------------------\n")

# Menu principal
while True:
    try:
        opcoes = int(input("\nO que você deseja fazer?\n(1) Saque\n(2) Depósito\n(3) Extrato\n(4) Sair\n→ "))
        if opcoes == 1:
            saque()
        elif opcoes == 2:
            deposito()
        elif opcoes == 3:
            extrato()
        elif opcoes == 4:
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Digite uma opção válida!")
    except ValueError:
        print("Digite apenas números!")
