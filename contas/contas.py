from abc import ABC, abstractmethod
from enum import Enum
from typing import Union
from bancos.agencias import Agencias


class TipoConta(Enum):
    corrente = 1
    poupanca = 2


class TipoCliente(Enum):
    fisica = 1
    juridica = 2


class Contas(ABC, Agencias):
    def __init__(self, agencia: str, codigo: int, banco: str, cpf: str, tipo_conta: TipoConta, tipo_cliente: TipoCliente,
                 saldo: float = 0, cnpj: str = None):
        Agencias.__init__(self, agencia, codigo, banco)
        self.__cpf = cpf
        self.__saldo = saldo
        if cnpj is not None:
            self.__cnpj = cnpj
        self.tipo_conta = tipo_conta
        self.tipo_cliente = tipo_cliente

    @property
    def cpf(self):
        return self.__cpf

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo: float):
        if not isinstance(saldo, (int, float)):
            raise ValueError("O Saldo deve conter números")
        self.__saldo = saldo

    def deposito(self, valor: float) -> bool:
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito deve conter números")
        elif valor < 0:
            raise ValueError("Para deposito informe um valor valido não negativo")
        self.__saldo += valor
        return True

    @abstractmethod
    def saque(self, valor: float):
        pass

    @abstractmethod
    def transferencia(self, valor: float, destino):
        pass
