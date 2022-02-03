class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adc_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def população(self):
        return sum([c.população for c in self.cidades])


class Cidade:
    def __init__(self, nome, população):
        self.nome = nome
        self.população = população
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, população={self.população}, estado={self.estado})"


pb = Estado("Paraiba", "PB")
pb.adc_cidade(Cidade("Cajazeiras", 62576))
pb.adc_cidade(Cidade("João Pessoa", 817511))
pb.adc_cidade(Cidade("Patos", 108192))

sp = Estado("São Paulo", "SP")
sp.adc_cidade(Cidade("São Paulo", 12396372))
sp.adc_cidade(Cidade("Guarulhos", 1379182))
sp.adc_cidade(Cidade("Hortolandia", 234259))

ce = Estado("Ceará", "CE")
ce.adc_cidade(Cidade("Mauriti", 48370))
ce.adc_cidade(Cidade("Juazeiro do Norte", 255648))
ce.adc_cidade(Cidade("Brejo Santo", 49842))

for estado in [pb, sp, ce]:
    print(f"Estado: {estado.nome} Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} População: {cidade.população}")
    print(f"Soma da população das cidades: {estado.população()}\n")


