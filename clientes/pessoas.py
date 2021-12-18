from abc import ABC, abstractmethod
from enderecos.endereco import Endereco


class Pessoas(ABC, Endereco):
    def __init__(self, nome: str, idade: int, rua: str, casa: int, bairro: str, cep: int = None):
        super().__init__(rua, casa, bairro, cep)
        self.nome = nome
        self._idade = idade

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if not idade >= 18:
            raise ValueError("Para realizar cadastro tem que ser maior de idade")
        self._idade = idade



