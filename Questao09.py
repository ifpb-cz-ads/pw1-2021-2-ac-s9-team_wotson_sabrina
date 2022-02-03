class Conta:
    def __init__(self, cliente, número, saldo=0):
        self.saldo = 0
        self.cliente = cliente
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        for cliente in self.cliente:
            print(" CC N°%s Saldo: %10.2f" %
                  (self.número, self.saldo))
            print(f"Nome: {cliente.nome}\nTelefone: {cliente.telefone}\n")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True;
        else:
            print("Valor insuficiente para saque.")
            return False;

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, cliente, número, saldo=0, limite=0):
        Conta.__init__(self, cliente, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True;
        else:
            return ContaEspecial.saque(self, valor)