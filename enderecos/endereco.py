class Endereco:
    def __init__(self, rua: str, casa: int, bairro: str, cep: int = 40000000):
        self.rua = rua
        self.casa = casa
        self.bairro = bairro
        if cep is None:
            self.cep = 40000000
        else:
            self.cep = cep

    def __str__(self):
        return f'''Rua: {self.rua}, Nº: {self.casa}
Bairro: {self.bairro}, Cep: {self.cep}'''
