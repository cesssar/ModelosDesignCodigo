from classes import *

class ClienteFactory:

    '''def criar_cliente(self, tipo, nome, documento):
        if tipo == 'pf':
            return ClientePF(nome, documento)
        elif tipo == 'pj':
            return ClientePJ(nome, documento)
        else:
            raise ValueError("Tipo de cliente não suportado!")
    '''

    def criar_cliente(self, tipo, nome, documento):
        try:
            return {
                'pf': ClientePF(nome, documento),
                'pj': ClientePJ(nome, documento)
            }[tipo]
        except KeyError:
            raise ValueError(f'Tipo de cliente inválido: {tipo}')