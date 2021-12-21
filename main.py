from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca


def main():
    cl1 = PessoaFisica('Antonio', 35, 'Cam 47', 167, 'Gleba-E', '54615891728', 42808193)
    cl3 = PessoaJuridica('Olinfor', '14376985000135', cl1)
    conta1 = ContaCorrente('Camaçari', 341, 'ITAU', cliente=cl1)
    conta2 = ContaCorrente('Lauro de Freitas', 7400, 'Caixa', empresa=cl3)
    conta3 = ContaPoupanca('Camaçari', 341, 'ITAU', cliente=cl1)
    conta4 = ContaPoupanca('Lauro de Freitas', 7400, 'Caixa', empresa=cl3)

    conta4.deposito(10000)
    conta1.deposito(500)
    conta1.saque(100)
    print(conta1)
    conta2.saque(1000)
    print(conta2)

    conta3.deposito(1000)
    conta3.saque(100)
    print(conta3)
    print(conta1)

    print(conta3.transferencia(500, conta1))
    print(conta3)
    print(conta1)

    conta4.transferencia(5000, conta2)
    print(conta4)
    print(conta2)


if __name__ == '__main__':
    main()
