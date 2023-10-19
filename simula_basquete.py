import random

def gera_resultados():
    pontosA = random.randint(75, 130)
    pontosB = random.randint(75, 130)
    while pontosA == pontosB:
        pontosB = random.randint(75, 130)
    return [pontosA, pontosB]

def mata_mata(timeA, timeB, arquivo):
    vitA = 0
    vitB = 0
    while vitA < 4 and vitB < 4:
        placar = gera_resultados()
        arquivo.write(f"{timeA} {placar[0]} X {placar[1]} {timeB}\n")
        if placar[0] > placar[1]:
            vitA = vitA + 1
        else:
            vitB = vitB + 1

    if vitA == 4:
        return timeA
    else:
        return timeB

leste = ["Knicks", "Nets", "Celtics", "76Sixers", "Bucks", "Cavaliers", "Hornets", "Bulls"]

oeste = ["Lakers", "Warriors", "Nuggets", "Suns", "Grizzlers", "Heat", "Raptors", "Clippers"]

arq = open("resultado.txt", 'w')

while len(leste) > 1:
    aux_leste = []
    aux_oeste = []
    i = 0
    j = len(leste) - 1

    while i < j:
        vencedor = mata_mata(leste[i], leste[j], arq)
        aux_leste.append(vencedor)
        vencedor = mata_mata(oeste[i], oeste[j], arq)
        aux_oeste.append(vencedor)
        i = i + 1
        j = j - 1

    leste = aux_leste
    oeste = aux_oeste

vencedor = mata_mata(leste[0], oeste [0], arq)
print("Vencedor: ", vencedor) 
# print(aux_leste)
# print(aux_oeste)
arq.close()