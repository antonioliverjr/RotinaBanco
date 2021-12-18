from clientes.pessoa_fisica import PessoaFisica
from clientes.pessoa_juridica import PessoaJuridica
from contas.conta_corrente import ContaCorrente
from contas.conta_poupanca import ContaPoupanca

if __name__ == '__main__':
    cl1 = PessoaFisica('Antonio', 35, 'Cam 47', 167, 'Gleba-E', '54615891728', 42808193)
    cl3 = PessoaJuridica('Olinfor', '14376985000135', cl1)
    conta1 = ContaCorrente('Camaçari', 341, 'ITAU', cliente=cl1)
    conta2 = ContaCorrente('Lauro de Freitas', 7400, 'Caixa', empresa=cl3)
    conta3 = ContaPoupanca('Camaçari', 341, 'ITAU', cliente=cl1)
    conta4 = ContaPoupanca('Lauro de Freitas', 7400, 'Caixa', empresa=cl3)