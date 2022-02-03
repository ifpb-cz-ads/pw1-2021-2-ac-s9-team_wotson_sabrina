class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %
              (self.número, self.saldo))

    def EfetuarSaque(self, valor):
        return self.saldo >= valor

    def saque(self, valor):
        if self.EfetuarSaque(valor):
            self.saldo -= valor
            self.operações.append(["Saque:", valor])
            return True
        else:
            print("Seu saldo é insuficiente para saque.")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))
        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def EfetuarSaque(self, valor):
        return self.saldo + self.limite >= valor
