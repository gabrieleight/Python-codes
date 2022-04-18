class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo objeto... Localização: {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print(f"O saldo da conta do titular {self.titular} é de R$ {self.saldo:.2f}")
    
    def deposita(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        self.saldo -= valor
        

conta1 = Conta(496256, 'Gabriel Gilberto', 660, 2500)
conta2 = Conta(496854, 'Emmanuel Nicolas', 5500, 10000)

print(conta1.saldo)
conta1.extrato()
print(conta2.saldo)
conta2.extrato()
conta1.deposita(5000)
conta1.extrato()
conta2.sacar(5000)
conta2.extrato()