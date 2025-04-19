class conta:
    def __init__(self, saldo, numero_conta, agencia, historico):
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.agencia = agencia
        self.historico = []

class ContaCorrente(conta):
    def __init__(self, saldo, numero_conta, agencia, historico, limite = 500, limite_saques = 500):
        super().__init__(saldo, numero_conta, agencia, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self,endereco = None, contas = None):
        self.endereco = endereco
        self.contas = contas

class PessoaFisica(Cliente):
    def __init__(self, cpf , nome, data_Nascimento):
        super().__init__(None, [])
        self.cpf = cpf
        self.nome = nome 
        self.data_Nascimento = data_Nascimento

def CriarUsuario():
    while 1:
        try:
            cpf = int(input("Digite o numero do Seu CPF"))
            nome = input("Digite o seu nome")
            dt_nascimento = input("Digite sua Data de Nascimento")

            cliente = PessoaFisica(cpf , nome , dt_nascimento)
            clientes = []
            clientes.append(cliente)
            break
        except ValueError:
            print("Digite um Valor Valido!!") 

def main(): 
    while 1:
        Entrada = int(input("Bem Vindo!!\n[1]Criar Usuario\n[2]Criar Conta\n[3]Saque\n[4]Deposito\n[5]Sair"))

        if Entrada == 1:
            CriarUsuario()
        elif Entrada == 2:
            pass
        elif Entrada == 3:
            pass
        elif Entrada == 4:
            pass
        elif Entrada == 5:
            pass
        else:
            print("Digite um Valor valido!!")
main()