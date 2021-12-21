from typing import Union
from contas.contas import Contas, TipoConta, TipoCliente
from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica


class ContaPoupanca(Contas):
    def __init__(self, agencia: str, codigo: int, banco: str, saldo: float = 0, cliente: PessoaFisica = None,
                 empresa: PessoaJuridica = None):
        if cliente is not None:
            if empresa is not None:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, TipoConta.poupanca, TipoCliente.juridica,
                                saldo, empresa.cnpj)
                self.cliente = cliente
                self.empresa = empresa
            else:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, TipoConta.poupanca, TipoCliente.fisica,
                                saldo)
                self.cliente = cliente
                self.empresa = empresa
        elif empresa is not None:
            Contas.__init__(self, agencia, codigo, banco, empresa.cpf, TipoConta.poupanca, TipoCliente.juridica,
                            saldo, empresa.cnpj)
            self.empresa = empresa
            self.cliente = cliente
        else:
            raise ValueError("Para abertura de conta, informe um objeto cliente ou empresa")

    def __str__(self):
        if self.empresa is not None:
            return f'''Conta Poupança PJ
Banco: {self.banco}
Agencia: {self.agencia}
Nome Empresa: {self.empresa.nome_fantasia}
Responsavel: {self.empresa.nome}
Endereço: {self.empresa.rua}, Nº: {self.empresa.casa}
Bairro: {self.empresa.bairro}
Cep: {self.empresa.cep}
Saldo: {self.saldo}
'''
        else:
            return f'''Conta Poupança PF
Banco: {self.banco}
Agencia: {self.agencia}
Nome Cliente: {self.cliente.nome}
Idade: {self.cliente.idade}
Endereço: {self.cliente.rua}, Nº: {self.cliente.casa}
Bairro: {self.cliente.bairro}
Cep: {self.cliente.cep}
Saldo: {self.saldo}
'''

    def saque(self, valor: float) -> bool:
        if not isinstance(valor, (int, float)):
            raise ValueError("Informe um valor válido")
        if not valor > 0:
            raise ValueError("Informe um valor positivo")

        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Está conta não possui saldo e nem limite para saque!")
            return False

    def transferencia(self, valor: float, destino) -> Union[bool, str]:
        """Transferência entre contas.

        O método deve receber um valor e um objeto de Conta Corrente ou Conta Poupança.
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("Informe um valor válido")
        if not valor > 0:
            raise ValueError("Informe um valor positivo")

        if destino is not None:
            if self.saque(valor):
                if destino.deposito(valor):
                    if destino.tipo_cliente.value == 1:
                        return f'''Transferência Realizada com sucesso para conta de {destino.cpf}!'''
                    else:
                        return f'''Transferência Realizada com sucesso para conta de {destino.cnpj}!'''
            return False
        return False
