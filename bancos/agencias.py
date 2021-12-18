class Agencias:
    def __init__(self, agencia: str, codigo: int, banco: str):
        self.codigo = codigo
        self.banco = banco.upper()
        self._agencia = agencia.upper()

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, agencia):
        if not len(agencia) >= 5:
            raise ValueError("O nome da agência deve ter ao menos 5 caracteres")
        self._agencia = agencia

    def __str__(self):
        return f'''
Agencia {self.banco}
Numero: {self.codigo}
Local: {self.agencia}
'''
