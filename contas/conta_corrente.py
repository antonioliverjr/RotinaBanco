from typing import Union
from contas.contas import Contas, TipoConta, TipoCliente
from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica


class ContaCorrente(Contas):
    def __init__(self, agencia: str, codigo: int, banco: str, saldo: float = 0, limite: float = 100,
                 cliente: PessoaFisica = None, empresa: PessoaJuridica = None):
        if cliente is not None:
            if empresa is not None:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, TipoConta.corrente, TipoCliente.juridica,
                                saldo, empresa.cnpj)
                self._limite = limite
                self._limite_especial = limite * 10
                self.cliente = cliente
                self.empresa = empresa
            else:
                Contas.__init__(self, agencia, codigo, banco, cliente.cpf, TipoConta.corrente, TipoCliente.fisica,
                                saldo)
                self._limite = limite
                self.cliente = cliente
                self.empresa = empresa
        elif empresa is not None:
            Contas.__init__(self, agencia, codigo, banco, empresa.cpf, TipoConta.corrente, TipoCliente.juridica,
                            saldo, empresa.cnpj)
            self._limite = limite
            self._limite_especial = limite * 10
            self.empresa = empresa
            self.cliente = cliente
        else:
            raise ValueError("Para abertura de conta, informe um objeto cliente ou empresa")

    @property
    def limite(self):
        if self.saldo >= 0:
            return self._limite
        if self.saldo < 0 and abs(self.saldo) > self._limite:
            return 0
        return self._limite - abs(self.saldo)

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def limite_especial(self):
        if self.saldo >= 0:
            return self._limite_especial
        if self.saldo < 0 and self.saldo < -self._limite:
            return (self._limite_especial + self._limite) - abs(self.saldo)

    @limite_especial.setter
    def limite_especial(self, limite_especial):
        self._limite_especial = limite_especial

    def __str__(self):
        if self.tipo_cliente.value == 2:
            return f'''Conta Corrente PJ
Banco: {self.banco}
Agencia: {self.agencia}
Nome Empresa: {self.empresa.nome_fantasia}
Responsavel: {self.empresa.nome}
Endereço: {self.empresa.rua}, Nº: {self.empresa.casa}
Bairro: {self.empresa.bairro}
Cep: {self.empresa.cep}
Saldo: {self.saldo} / Limite: {self.limite} / Limite Especial: {self.limite_especial}
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

    def saque(self, valor: float) -> bool:
        if not isinstance(valor, (int, float)):
            raise ValueError("Informe um valor válido")
        if not valor > 0:
            raise ValueError("Informe um valor positivo")

        if self.tipo_cliente.value == 2:
            if (self.saldo + self._limite + self._limite_especial) >= valor:
                self.saldo -= valor
                return True
            else:
                print("Está conta não possui saldo e nem limite para saque!")
                return False
        else:
            if (self.saldo + self._limite) >= valor:
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
