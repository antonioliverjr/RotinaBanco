from abc import ABC, abstractmethod
from bancos.agencias import Agencias


class Contas(ABC, Agencias):
    def __init__(self, agencia: str, codigo: int, banco: str, cpf: str, saldo: float = 0, cnpj: str = None):
        Agencias.__init__(self, agencia, codigo, banco)
        self.__cpf = cpf
        self.__saldo = saldo
        if cnpj is not None:
            self.__cnpj = cnpj

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
    def saldo(self, saldo):
        if not saldo > 0:
            raise ValueError("O Saldo não pode ser negativo")
        elif not isinstance(saldo, (int, float)):
            raise ValueError("O Saldo deve conter números")
        self.__saldo = saldo

    def deposito(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito deve conter números")
        elif valor < 0:
            raise ValueError("Para deposito informe um valor valido não negativo")
        self.__saldo += valor

    @abstractmethod
    def saque(self):
        pass
