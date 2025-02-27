from cliente import Cliente

class ClientePF(Cliente):

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
    
    def exibir_dados(self):
        print(f'Cliente PF {self.nome} do CPF {self.cpf}')

class ClientePJ(Cliente):

    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj

    def exibir_dados(self):
        print(f'Cliente PJ {self.nome} com CNPJ {self.cnpj}')