class Carro:
    def __init__(self, marca, cor, modelo):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        
    def Ligar(self):
        print("Vruuuuuum hmmmmmmmmmmmmmmm")
        
    def Desligar(self):
        print("Hmmmmmmmmm piii piii piii")
        
    def Parabrisas(self):
        sn = input("Você desejar ligar os parabrisas (s/n): ").lower()
        if sn == 's':
            print("Parabrisas ligado!!!")
        else:
            print("Parabrisas continua desligado")
            
    def informaçõesSobreEsseCarro(self):
        print(f"A marca do carro é {self.marca}, o modelo é o {self.modelo}, de cor {self.cor}")
        

carro1 = Carro("Chevrolet", "Branco-Gelo", "Onix")

carro1.informaçõesSobreEsseCarro()
carro1.Ligar()
carro1.Parabrisas()