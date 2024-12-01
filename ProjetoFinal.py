import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/mauad/AtividadesUFRJ/ORGdados/ProjetoFinal/pokedex.csv')

colunas = [df.columns]

df.describe

df = df.fillna("mono_type") # Preenche os tipos secundários de pokemons de apenas um tipo

#Cria 18 dataframes para os 18 tipos de pokemon

tipo_agua1 = df[df["Type 1"] == "Water"]
tipo_agua2 = df[df["Type 2"] == "Water"]
tipo_agua = pd.concat([tipo_agua1, tipo_agua2])

tipo_fogo1 = df[df["Type 1"] == "Fire"]
tipo_fogo2 = df[df["Type 2"] == "Fire"]
tipo_fogo = pd.concat([tipo_fogo1, tipo_fogo2])

tipo_grama1 = df[df["Type 1"] == "Grass"]
tipo_grama2 = df[df["Type 2"] == "Grass"]
tipo_grama = pd.concat([tipo_grama1, tipo_grama2])

tipo_eletrico1 = df[df["Type 1"] == "Electric"]
tipo_eletrico2 = df[df["Type 2"] == "Electric"]
tipo_eletrico = pd.concat([tipo_eletrico1, tipo_eletrico2])

tipo_fantasma1 = df[df["Type 1"] == "Ghost"]
tipo_fantasma2 = df[df["Type 2"] == "Ghost"]
tipo_fantasma = pd.concat([tipo_fantasma1, tipo_fantasma2])

tipo_normal1 = df[df["Type 1"] == "Normal"]
tipo_normal2 = df[df["Type 2"] == "Normal"]
tipo_normal = pd.concat([tipo_normal1, tipo_normal2])

tipo_psiquico1 = df[df["Type 1"] == "Psychic"]
tipo_psiquico2 = df[df["Type 2"] == "Psychic"]
tipo_psiquico = pd.concat([tipo_psiquico1, tipo_psiquico2])

tipo_rock1 = df[df["Type 1"] == "Rock"]
tipo_rock2 = df[df["Type 2"] == "Rock"]
tipo_rock = pd.concat([tipo_rock1, tipo_rock2])

tipo_voador1 = df[df["Type 1"] == "Flying"]
tipo_voador2 = df[df["Type 2"] == "Flying"]
tipo_voador = pd.concat([tipo_voador1, tipo_voador2])

tipo_terra1 = df[df["Type 1"] == "Ground"]
tipo_terra2 = df[df["Type 2"] == "Ground"]
tipo_terra = pd.concat([tipo_terra1, tipo_terra2])

tipo_inseto1 = df[df["Type 1"] == "Bug"]
tipo_inseto2 = df[df["Type 2"] == "Bug"]
tipo_inseto = pd.concat([tipo_inseto1, tipo_inseto2])

tipo_dragao1 = df[df["Type 1"] == "Dragon"]
tipo_dragao2 = df[df["Type 2"] == "Dragon"]
tipo_dragao = pd.concat([tipo_dragao1, tipo_dragao2])

tipo_sombrio1 = df[df["Type 1"] == "Dark"]
tipo_sombrio2 = df[df["Type 2"] == "Dark"]
tipo_sombrio = pd.concat([tipo_sombrio1, tipo_sombrio2])

tipo_lutador1 = df[df["Type 1"] == "Fighting"]
tipo_lutador2 = df[df["Type 2"] == "Fighting"]
tipo_lutador = pd.concat([tipo_lutador1, tipo_lutador2])

tipo_gelo1 = df[df["Type 1"] == "Ice"]
tipo_gelo2 = df[df["Type 2"] == "Ice"]
tipo_gelo = pd.concat([tipo_gelo1, tipo_gelo2])

tipo_venenoso1 = df[df["Type 1"] == "Poison"]
tipo_venenoso2 = df[df["Type 2"] == "Poison"]
tipo_venenoso = pd.concat([tipo_venenoso1, tipo_venenoso2])

tipo_aco1 = df[df["Type 1"] == "Steel"]
tipo_aco2 = df[df["Type 2"] == "Steel"]
tipo_aco = pd.concat([tipo_aco1, tipo_aco2])

tipo_fada1 = df[df["Type 1"] == "Fairy"]
tipo_fada2 = df[df["Type 2"] == "Fairy"]
tipo_fada = pd.concat([tipo_fada1, tipo_fada2])

# Cria um vetor com todos os DataFrames dos pokemons separados por tipo
pokemons_por_tipo = [tipo_agua, tipo_fogo, tipo_grama, tipo_eletrico, tipo_fantasma, tipo_normal,
                     tipo_psiquico, tipo_rock, tipo_voador, tipo_inseto, tipo_terra, tipo_dragao, tipo_sombrio, tipo_lutador,
                     tipo_gelo, tipo_venenoso, tipo_aco, tipo_fada]

nome_dos_tipos = ["Water", "Fire", "Grass", "Eletric", "Ghost", "Normal", "Psychic", "Rock", "Flying", "Bug", "Ground", "Dragon", "Dark", "Fighting", "Ice", "Poison", "Steel", "Fairy"]

atributos = ["HP", "Attack", "Defense", "SP. Atk.", "SP. Def", "Speed"]

#Dicionário com chave = nome dos tipos // valor = tipo [dataframe]

dic_nome_tipo = {}
for i in range(len(nome_dos_tipos)):
  dic_nome_tipo[nome_dos_tipos[i]] = pokemons_por_tipo[i]


#Média de atributos de todos os pokemons
media_atributos_pokedex = []
for atributo in atributos:
  print(f"{atributo}: ")
  print(f"{df[atributo].mean():.2f}")
  media_atributos_pokedex.append(df[atributo].mean())

  print()
#Os valores estão "soltos", mas a ordem dos atributos é sempre: ["HP", "Attack", "Defense", "SP. Atk.", "SP. Def", "Speed"]

print(media_atributos_pokedex)


print("Média de cada atributo para cada tipo")
print()
dic_maior_media_cada_tipo = {}

for nome, tipo in dic_nome_tipo.items():

  dic_maior_media_cada_tipo[nome] =  tipo[atributos].mean().max()

  print(f"Nome: {nome}")
  print(f"Hp:  {tipo['HP'].mean():.2f}")
  maior = tipo['HP'].mean()
  nome_maior = "HP"

  print(f"Attack:  {tipo['Attack'].mean():.2f}")
  if tipo['Attack'].mean() > maior:
    maior = tipo['Attack'].mean()
    nome_maior = "Attack"

  print(f"Defense:  {tipo['Defense'].mean():.2f}")
  if tipo['Defense'].mean() > maior:
    maior = tipo['Defense'].mean()
    nome_maior = "Defense"

  print(f"SP. Atk.:  {tipo['SP. Atk.'].mean():.2f}")
  if tipo['SP. Atk.'].mean() > maior:
    maior = tipo['SP. Atk.'].mean()
    nome_maior = "SP. Atk."

  print(f"SP. Def:  {tipo['SP. Def'].mean():.2f}")
  if tipo['SP. Def'].mean() > maior:
    maior = tipo['SP. Def'].mean()
    nome_maior = "SP. Def"

  print(f"Speed:  {tipo['Speed'].mean():.2f}")
  if tipo['Speed'].mean() > maior:
    maior = tipo['Speed'].mean()
    nome_maior = "Speed"

  print(f"Maior média: {nome_maior} com {maior:.2f}")

  print()
  print()

  dic_maior_media_cada_tipo[nome] =  [nome_maior, tipo[atributos].mean().max()]

print("Atributo mais forte de cada pokemon, e o valor: \n")

for nome, valor in dic_maior_media_cada_tipo.items():
  print(f"{nome:<10} : {valor[0]} = {valor[1]:.2f}")

print("\n\n")

#Analisando os tipos mais COMUNS / RAROS
quantidade_de_tipos = [] #guarda, na ordem dos tipos, a quantidade de cada

for nome, tipo in dic_nome_tipo.items():
  quantidade_de_tipos.append(len(tipo))

mais_comum = nome_dos_tipos[quantidade_de_tipos.index(max(quantidade_de_tipos))]  # Nome do tipo mais comum

menos_comum = nome_dos_tipos[quantidade_de_tipos.index(min(quantidade_de_tipos))] # Nome do tipo menos comum


print(f"Tipo raro: {mais_comum} = {max(quantidade_de_tipos)}")
print(f"Tipo comum: {menos_comum} = {min(quantidade_de_tipos)}")
print("\n\n")


#Média de total mais alta
# Os mais fracos e mais fortes de cada tipo medidos pelo atributo "Total"

media_totais_tipo = [] # Grava as médias de totais de cada tipo na ordem da variável nome_
print("Média do atributo total de cada tipo: \n")
for nome, tipo in dic_nome_tipo.items(): #percorre o dicionário que tem {"nome_tipo" : tipo [dataframe]}
  print(f"{nome:<10}: {tipo['Total'].mean():.2f}")
  media_totais_tipo.append(tipo['Total'].mean()) #Pega a média do atual tipo

media_mais_forte = max(media_totais_tipo)
nome_tipo_mais_forte = nome_dos_tipos[media_totais_tipo.index(media_mais_forte)]

media_mais_fraca = min(media_totais_tipo)
nome_tipo_mais_fraco = nome_dos_tipos[media_totais_tipo.index(media_mais_fraca)]

print()
print()
print(f"Tipo mais forte: {nome_tipo_mais_forte}")
print(f"Tipo mais fraco: {nome_tipo_mais_fraco}")


#Os top 10 pokemons de cada atributo

top_10_cada_atributo = [] # Variável guarda 6 dataframes na ordem dos atributos (6 atributos)
for atributo in atributos:

  top_10_cada_atributo.append(df[["Name", atributo]].sort_values(by=atributo, ascending=False).head(10))

  # ATENÇÃO: ESCOLHA UMA DAS LINHAS. A DE BAXIO GUARDA O DATASET COMPLETO DO TOP 10_POKEMONS.
  # A DE CIMA GUARDA O DATASET SÓ COM NOME, INDEX E O RESPECTIVO ATRIBUTO ANALISADO
  # SE JULGAREM QUE VÃO UTILIZAR VÁRIAS INFORMAÇÕES NA ANÁLISE, USE A DE BAIXO

  """top_10_cada_atributo.append(df.sort_values(by=atributo, ascending=False).head(10))"""

for i in range(6):
  print(top_10_cada_atributo[i])
  print()

  #O top 5 de atributo "Total" de cada tipo de pokemon

top_5_total_cada_tipo = {} #Dicionário que guarda: {"Nome_do_tipo" : Top 5 totais do tipo [dataframe]}

for nome, tipo in dic_nome_tipo.items():
  top_5_total_cada_tipo[nome] = tipo[["Name", "Total"]].sort_values("Total", ascending = False).head(5) #Caso queiram todo o dataset, basta remover [["Name", "Total"]] de df
  print(f"Top 5 de {nome}:")
  print(top_5_total_cada_tipo[nome])

  print()
  print()

# Parte da configuração do site
def main():
  st.set_page_config(
      page_title="Análise interativa da pokedex",
      page_icon=":pokeball:",
      layout="wide"
  )
  st.title("Feito com Pandas e Streamlit")
  st.write("Dados utilizados: ")
  st.dataframe(df)
  
main()