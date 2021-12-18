from clientes.pessoa_fisica import PessoaFisica


class PessoaJuridica(PessoaFisica):
    def __init__(self, nome_fantasia: str, cnpj: str, responsavel: PessoaFisica):
        super().__init__(responsavel.nome, responsavel.idade, responsavel.rua, responsavel.casa, responsavel.bairro,
                         responsavel.cpf, responsavel.cep)
        self.nome_fantasia = nome_fantasia
        self.__cnpj = cnpj

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        if not len(cnpj) == 14:
            raise ValueError("CNPJ deve conter 14 digitos!")
        self.__cnpj = cnpj

    def __str__(self):
        return f'''Cliente PJ
Nome Fantasia: {self.nome_fantasia}
Responsável: {self.nome}
Endereço: {self.rua}, Nº: {self.casa}
Bairro: {self.bairro}
Cep: {self.cep}
'''