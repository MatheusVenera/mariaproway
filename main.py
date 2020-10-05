from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import from_html

quantidade_jogos = 0
lista_jogos = []
lista_pontuação = []
minimo = 1001
maximo = 0
quebra_min = 0
quebra_max = 0

class Jogo():

    def __init__(self, id, placar, minimo, maximo, quebra_min, quebra_max):
        self.id = id
        self.placar = placar
        self.minimo = minimo
        self.maximo = maximo
        self.quebra_min = quebra_min
        self.quebra_max = quebra_max

while True:
    opcao = int(input("Deseja inserir dados (1) ou buscar dados (2)?\n"))
    if opcao == 1:
        while True:
            pontuação = int(input("Insira a pontuação deste jogo: \n"))
            if pontuação > 1000:
                print("A pontuação não pode ser maior que 1000!")
            elif pontuação <= 1000:
                break
        quantidade_jogos += 1
        lista_pontuação.append(pontuação)
        if quantidade_jogos == 1:
            minimo = pontuação
            maximo = pontuação
            quebra_min = 0
            quebra_max = 0
        elif quantidade_jogos != 1:
            if pontuação < minimo:
                quebra_min += 1
            elif pontuação > maximo:
                quebra_max += 1
            minimo = min(lista_pontuação)
            maximo = max(lista_pontuação)

        lista_jogos.append(Jogo(quantidade_jogos, pontuação, minimo, maximo, quebra_min, quebra_max))
    elif opcao == 2:
        tabela = PrettyTable()
        tabela.field_names = ["Jogo", "Placar", "Mínimo", "Máximo", "Quebra Mín", "Quebra Máx"]
        tabela.padding_width = 1
        for i in range(len(lista_jogos)):
            tabela.add_row([lista_jogos[i].id, lista_jogos[i].placar, lista_jogos[i].minimo, lista_jogos[i].maximo, lista_jogos[i].quebra_min, lista_jogos[i].quebra_max])
        print(tabela)