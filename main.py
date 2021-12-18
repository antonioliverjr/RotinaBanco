from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica
from contas.conta_corrente import ContaCorrente

if __name__ == '__main__':
    cl1 = PessoaFisica('Antonio', 35, 'Cam 47', 167, 'Gleba-E', '54615891728', 42808193)
    print(cl1)

    cl3 = PessoaJuridica('Olinfor', '14376985000135', cl1.nome, cl1.idade, cl1.rua, cl1.casa, cl1.bairro , cl1.cpf, cl1.cep)
    print(cl3)

    conta1 = ContaCorrente('Camaçari', 341, 'ITAU', cliente=cl1)
    print(conta1)

    conta2 = ContaCorrente('Lauro de Freitas', 7400, 'Caixa', empresa=cl3)
    print(conta2)
