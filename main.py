from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica


if __name__ == '__main__':
    cl1 = PessoaFisica('Antonio', 35, 'Cam 47', 167, 'Gleba-E', '02259144500', 42808193)
    print(cl1)
    cl2 = PessoaFisica('Cassia', 29, 'Cam 47', 167, 'Gleba-E', '06459180598')
    print(cl2)

    cl3 = PessoaJuridica('Olinfor', '14376985000135', cl1.nome, cl1.idade, cl1.rua, cl1.casa, cl1.bairro ,cl1.cpf, cl1.cep)
    print(cl3)
