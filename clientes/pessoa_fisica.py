from clientes.pessoas import Pessoas


class PessoaFisica(Pessoas):
    def __init__(self, nome: str, idade: int, rua: str, casa: int, bairro: str, cpf: str, cep: int = None):
        super().__init__(nome, idade, rua, casa, bairro, cep)
        self.__cpf = cpf

    @property
    def cpf(self):
        return '{:*>11}'.format('')

    @cpf.setter
    def cpf(self, cpf):
        if not len(cpf) == 11:
            raise ValueError("CPF deve conter 11 digitos!")
        self.__cpf = cpf

    def __str__(self):
        return f'''Cliente PF
Nome: {self.nome}
Idade: {self.idade}
Endereço: {self.rua}, Nº: {self.casa}
Bairro: {self.bairro}
Cep: {self.cep}
'''
