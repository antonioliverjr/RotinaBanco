from contas.contas import Contas
from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica


class ContaCorrente(Contas):
    def __init__(self, agencia: str, codigo: int, banco: str, saldo: float = 0, limite: float = 100,
                 cliente: PessoaFisica = None, empresa: PessoaJuridica = None):
        if cliente is not None:
            if empresa is not None:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, saldo, empresa.cnpj)
                self.limite = limite
                self.limite_especial = limite * 10
                self.cliente = cliente
                self.empresa = empresa
            else:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, saldo)
                self.limite = limite
                self.cliente = cliente
                self.empresa = empresa
        elif empresa is not None:
            Contas.__init__(self, agencia, codigo, banco, empresa.cpf, saldo, empresa.cnpj)
            self.limite = limite
            self.limite_especial = limite * 10
            self.empresa = empresa
            self.cliente = cliente
        else:
            raise ValueError("Para abertura de conta, informe um objeto cliente ou empresa")

    def __str__(self):
        if self.empresa is not None:
            return f'''Conta Corrente PJ
Banco: {self.banco}
Agencia: {self.agencia}
Nome Empresa: {self.empresa.nome_fantasia}
Responsavel: {self.empresa.nome}
Endereço: {self.empresa.rua}, Nº: {self.empresa.casa}
Bairro: {self.empresa.bairro}
Cep: {self.empresa.cep}
Saldo: {self.saldo} - Limite: {self.limite} / Limite Especial: {self.limite_especial}
'''
        else:
            return f'''Conta Corrente PF
Banco: {self.banco}
Agencia: {self.agencia}
Nome Cliente: {self.cliente.nome}
Idade: {self.cliente.idade}
Endereço: {self.cliente.rua}, Nº: {self.cliente.casa}
Bairro: {self.cliente.bairro}
Cep: {self.cliente.cep}
Saldo: {self.saldo} - Limite: {self.limite}
'''

    def saque(self):
        pass
