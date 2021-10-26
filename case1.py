import matplotlib.pyplot
import pandas as pd
from matplotlib import pyplot as plt
from pygame import mixer
import numpy as np

athletes = "/home/leandro/Documentos/trilha-Python/case/final/Athletes.xlsx"
coaches = "/home/leandro/Documentos/trilha-Python/case/final/Coaches.xlsx"
entries_gender = "/home/leandro/Documentos/trilha-Python/case/final/EntriesGender.xlsx"
medals = "/home/leandro/Documentos/trilha-Python/case/final/Medals.xlsx"
teams = "/home/leandro/Documentos/trilha-Python/case/final/Teams.xlsx"

athletes_df = pd.read_excel(athletes)
entriesGender_df = pd.read_excel(entries_gender)
medals_df = pd.read_excel(medals)
teams_df = pd.read_excel(teams)

import warnings  # ignorar warning dado por coaches.xlsx

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    coaches_df = pd.read_excel(coaches, engine="openpyxl")


def total_atletas():
    print(f"A quantidade de atletas que disputaram as Olimpíadas de Tokyo 2020 | 2021 foram {len(athletes_df)} atletas")
    print(type(len(athletes_df)))


def total_generos():
    print(f"Total de Homens que participaram da Olimpíada foi {entriesGender_df['Male'].sum()}")
    print(f"Total de mulheres que participaram da Olimpíada foi {entriesGender_df['Female'].sum()}")

    grupos = ['Homens', 'Mulheres']
    valores = [entriesGender_df['Male'].sum(), entriesGender_df['Female'].sum()]
    plt.bar(grupos, valores)
    plt.show()


def total_atle_espor():
    print(athletes_df.groupby(by='Discipline').size())


def total_meda_pais():
    x = 0

    while x < len(medals_df):
        medals_df["Total de medalhas"] = medals_df["Gold"] + medals_df["Silver"] + medals_df["Bronze"]
        print(f"o País   {medals_df.loc[x, 'Team/NOC']}  Possui  {medals_df.loc[x, 'Total de medalhas']} medalha(s)")

        x = x + 1

    print("\nA Seguir o Ranking de medalhas: ")
    sorted_df = medals_df.sort_values('Total de medalhas', ascending=False)
    print(f"\n{sorted_df}")


def pais_mais_ouro_prata_bronze():
    y = (medals_df["Gold"].argmax())
    x = medals_df.loc[y, "Gold"]
    print("País com maior número de moedas de ouro foi: " + medals_df.loc[y, "Team/NOC"] + f", com {x}  medalhas.")

    y = (medals_df["Silver"].argmax())
    z = medals_df.loc[y, "Silver"]
    print("País com maior número de moedas de prata foi: " + medals_df.loc[y, "Team/NOC"] + f", com {z}  medalhas.")

    y = (medals_df["Bronze"].argmax())
    t = medals_df.loc[y, "Bronze"]
    print("País com maior número de moedas de bronze foi: " + medals_df.loc[y, "Team/NOC"] + f", com {t}  medalhas.")

    grupos = ['Ouro', 'Prata', 'Bronze']
    valores = [x, z, t]
    plt.bar(grupos, valores)
    plt.show()


def pais_menos_ouro_prata_bronze():
    contador = 0
    y = (medals_df["Gold"].min())  # retona 0, o menor valar de medalhas de ouro
    while contador < len(medals_df):  # laço pra printar todos que tenham medalha 0
        if medals_df.loc[contador, "Gold"] == y:
            print("País com menor número de medalhas de ouro foi: " + medals_df.loc[
                contador, "Team/NOC"] + f", com {y}  medalhas.")
        contador = contador + 1

    print("\n")
    contador = 0
    y = (medals_df["Silver"].min())
    while contador < len(medals_df):
        if medals_df.loc[contador, "Silver"] == y:
            print("País com menor número de medalhas de prata foi: " + medals_df.loc[
                contador, "Team/NOC"] + f", com {y}  medalhas.")
        contador = contador + 1

    print("\n")
    contador = 0
    y = (medals_df["Bronze"].min())
    while contador < len(medals_df):
        if medals_df.loc[contador, "Bronze"] == y:
            print("País com menor número de medalhas de bronze foi: " + medals_df.loc[
                contador, "Team/NOC"] + f", com {y}  medalhas.")
        contador = contador + 1

def esportes_participantes():
    print("A seguir os Esportes que participaram das Olimpíadas de Tokyo 2020 | 2021 : ")
    print(entriesGender_df['Discipline'])


def esportes_homens_maisQ_mulheres():
    x = 0
    while x < len(entriesGender_df):
        if entriesGender_df.loc[x, "Female"] < entriesGender_df.loc[x, "Male"]:
            print(entriesGender_df.loc[x, "Discipline"])

        x = x + 1


def esportes_mulheres_maisQ_homens():
    x = 0
    while x < len(entriesGender_df):
        if entriesGender_df.loc[x, "Female"] > entriesGender_df.loc[x, "Male"]:
            print(entriesGender_df.loc[x, "Discipline"])

        x = x + 1


def qtd_treinadores_pais():
    print(coaches_df['NOC'].value_counts())


def pais_mais_treinadores():
    print(
        f"O País com mais treinadores é: {coaches_df['NOC'].value_counts()[:1].index.tolist()}")  # 1 pois quer apenas o primeiro


def qtd_treinadores_esporte():
    print(coaches_df['Discipline'].value_counts())

    #plotando o gráfico
    x = coaches_df['Discipline'].value_counts()
    x.plot(kind = 'pie', autopct = '%0.2f%%', figsize = (30,30))
    matplotlib.pyplot.show()





def time_por_esporte():
    group = teams_df.groupby(["Discipline", "Name"])
    print(group.size().reset_index(name='counts'))


if __name__ == '__main__':
    x = 0
    while x != 14:
        print("\n======== Bem vindo á tabela de dados da olimpíada de Tokio 2020 | 2021 ========\n")
        print("Selecione o número correspondente ao dado que você deseja: \n")
        print("1 - Total de atletas participantes. ")
        print("2 - Total de participantes homens e o total de participantes mulheres. ")
        print("3 - Total de participantes por esporte. ")
        print("4 - Total de medalhas por país e o ranking por medalhas totais ")
        print("5 - País com mais medalhas de ouro, prata e bronze. ")
        print("6 - País com menos medalhas de ouro, prata e bronze. ")
        print("7 - Lista com esportes participantes. ")
        print("8 - Lista de esportes com mais homens que mulheres. ")
        print("9 - Lista de esportes com mais mulheres que homens. ")
        print("10 - Quantidade de treinadores por país")
        print("11 - País com a maior quantidade de treinadores ")
        print("12 - Quantidade de treinadores por esporte. ")
        print("13 - Quanto times por esporte cada país tem. ")
        print("14 - Sair.\n\n")

        while True:  # tratando caso o usuário digite algo diferente de número
            try:
                x = int(input())
                break
            except ValueError:
                print("\nOops!  Você digitou uma opção inválida  tente de novo\n")

        if x == 1:
            total_atletas()

        elif x == 2:
            total_generos()

        elif x == 3:
            total_atle_espor()

        elif x == 4:
            total_meda_pais()

        elif x == 5:
            pais_mais_ouro_prata_bronze()

        elif x == 6:
            pais_menos_ouro_prata_bronze()

        elif x == 7:
            esportes_participantes()

        elif x == 8:
            esportes_homens_maisQ_mulheres()

        elif x == 9:
            esportes_mulheres_maisQ_homens()

        elif x == 10:
            qtd_treinadores_pais()

        elif x == 11:
            pais_mais_treinadores()

        elif x == 12:
            qtd_treinadores_esporte()

        elif x == 13:
            time_por_esporte()

        elif x == 14:
            print(
                "\nTabela de dados da olimpíada de Tokio 2020 | 2021 finalizada com sucesso, até mais e aproveite a música")
            mixer.init()
            mixer.music.load('audio.mp3')
            mixer.music.play()
            input("\nToque qualquer tecla para terminar o som\n")

        else:
            print("\nNÚMERO INVÁLIDO !!! :( tente novamente\n")
