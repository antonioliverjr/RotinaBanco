from abc import ABC, abstractmethod
from enderecos.endereco import Endereco


class Pessoas(ABC, Endereco):
    def __init__(self, nome: str, idade: int, rua: str, casa: int, bairro: str, cep: int = None):
        super().__init__(rua, casa, bairro, cep)
        self.nome = nome
        self.idade = idade




