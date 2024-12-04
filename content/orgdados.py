import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt


st.title("Análise interativa dos pokemon ")
page_icon=":pokeball:"
layout="wide"

df = pd.read_csv("pokedex.csv")

st.write("dataset utilizado: ") 
st.dataframe(df)


import os

# Caminho para a pasta das imagens

def printar_imagem(image):

    image_path = image

    # Verificar se o arquivo existe antes de exibir
    if os.path.exists(image_path):
        st.image(image_path, caption=" ", width=200, use_container_width=False)
    else:
        st.write(f"A imagem não foi encontrada no diretório.")



atributos = ["HP", "Attack", "Defense", "SP. Atk.", "SP. Def", "Speed"]

df = df.fillna("mono_type")
#"""Verificando se ainda há valores nulos"""
df.isna().sum()

todos = df[df["Index"] != False]

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

pokemons_por_geracao = []
pokemons_por_geracao.append(df.iloc[0:203,:]) #1
pokemons_por_geracao.append(df.iloc[204:317,:]) #2
pokemons_por_geracao.append(df.iloc[318:480,:]) #3
pokemons_por_geracao.append(df.iloc[481:605, :]) #4
pokemons_por_geracao.append(df.iloc[606:782, :]) #5
pokemons_por_geracao.append(df.iloc[783:870, :]) #6
pokemons_por_geracao.append(df.iloc[871:970, :]) #7
pokemons_por_geracao.append(df.iloc[971: 1079, :]) #8
pokemons_por_geracao.append(df.iloc[1080: 1214, :]) #9

pokemons_por_tipo = [todos, tipo_agua, tipo_fogo, tipo_grama, tipo_eletrico, tipo_fantasma, tipo_normal,
                     tipo_psiquico, tipo_rock, tipo_voador, tipo_inseto, tipo_terra, tipo_dragao, tipo_sombrio, tipo_lutador,
                     tipo_gelo, tipo_venenoso, tipo_aco, tipo_fada,pokemons_por_geracao[0],pokemons_por_geracao[1],
                     pokemons_por_geracao[2],pokemons_por_geracao[3],pokemons_por_geracao[4],pokemons_por_geracao[5],
                     pokemons_por_geracao[6],pokemons_por_geracao[7],pokemons_por_geracao[8]]

nome_dos_tipos = ["Todos", "Water", "Fire", "Grass", "Electric", "Ghost", "Normal", "Psychic", "Rock", "Flying", "Bug", "Ground", "Dragon",
 "Dark", "Fighting", "Ice", "Poison", "Steel", "Fairy",
"1ª Geração","2ª Geração","3ª Geração","4ª Geração","5ª Geração","6ª Geração","7ª Geração"
,"8ª Geração","9ª Geração"]

Cor_do_grafico = ["lavender", "blue","red","green","yellow","mediumpurple","silver","hotpink","gray","lightcyan","springgreen","burlywood",
"royalblue","black","firebrick","deepskyblue","blueviolet","slategrey","lightpink","red","gold","lime","lightcyan","grey","mediumblue",
"orange","aqua","darkviolet"]



#Dicionário com chave = nome dos tipos // valor = tipo [dataframe]
dic_nome_tipo = {}
for i in range(len(nome_dos_tipos)):
  dic_nome_tipo[nome_dos_tipos[i]] = pokemons_por_tipo[i]


else:

        
        fig = plt.figure(figsize=(12, 6))
        
        df["Type 1"].value_counts().plot(kind="bar", color=Cor_do_grafico[1], edgecolor="black")
        plt.title("Contagem de Pokémons por Tipo Primário", fontsize=16)
        plt.xlabel("Tipo Primário", fontsize=14)
        plt.ylabel("Quantidade", fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

        fig = plt.figure(figsize=(12, 6))
        
        df2 = df[df["Type 2"] != "mono_type"]

        df2["Type 2"].value_counts().plot(kind="bar", color=Cor_do_grafico[2], edgecolor="black")
        plt.title("Contagem de Pokémons por Tipo Secundário", fontsize=16)
        plt.xlabel("Tipo Primário", fontsize=14)
        plt.ylabel("Quantidade", fontsize=14)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        st.pyplot(fig)

st.write("Acima, temos um gráfico que mostra a quantidade de pokémon de cada tipo. Assim, permite-se analisar a variação de raridade dos tipos primários, concluindo que pokémon de tipo primário normal e água são os mais comuns, enquanto pokémon de fada e gelo são os mais raros.")
st.write("Também cabe observar, a partir do gráfico abaixo, a tendência de aumento da média dos status totais dos pokémon ao longo das gerações. Isso é uma manifestação do 'power creep', fenômeno comum em jogos competitivos caracterizado por aumentar drasticamente os níveis de poder à medida que novo conteúdo é adicionado.")

# Calculando a média dos status totais de cada geração
geracoes = ["1ª Geração", "2ª Geração", "3ª Geração", "4ª Geração", "5ª Geração", "6ª Geração", "7ª Geração", "8ª Geração", "9ª Geração"]
media_status_totais = []

for geracao in geracoes:
    # Obtendo o dataframe da geração
    df_geracao = dic_nome_tipo.get(geracao, pd.DataFrame())
    # Calculando a média do Total, se houver dados
    if not df_geracao.empty:
        media_status_totais.append(df_geracao["Total"].mean())
    else:
        media_status_totais.append(0)  # Caso não haja dados, usa 0 como valor padrão

# Criando o gráfico de linha para as médias dos status totais por geração
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(geracoes, media_status_totais, marker='o', color='blue', linestyle='-', linewidth=2, markersize=8)
ax.set_title("Média dos Status Totais por Geração", fontsize=16)
ax.set_xlabel("Gerações", fontsize=14)
ax.set_ylabel("Média dos Status Totais", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

st.write("Essa tendência, por sua vez, pode ser associada com os dados apresentados no gráfico abaixo, que mostra o número de pokémon 'especiais' (termo utilizado para pokémon lendários, míticos e paradoxos, com um padrão de alto poder e atributos) por cada geração. Assim, conclui-se que, quanto maior o número de pokémon especiais em uma geração, maior a média de status totais da geração tende a ser.")


fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(geracoes, [5, 6, 10, 14, 13, 6, 27, 12, 32], marker='o', color='red', linestyle='-', linewidth=2, markersize=8)
ax.set_title("Quantidade de Pokémon Especiais por Geração", fontsize=16)
ax.set_xlabel("Gerações", fontsize=14)
ax.set_ylabel("Quantidade de Especiais", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.7)
st.pyplot(fig)

st.write("As exceções a esse padrão são as gerações 4, 6 e 8. A quarta geração, apesar de não possuir uma quantidade tão grande de pokémon especiais, por apresentar lendários como Arceus e diversos pokémon com variantes Mega e Origem, possui uma média de atributos muito alta. Por outro lado, gerações que apresentam poucos especiais em comparação a suas médias de atributos, como a 6 e a 8, possuem essa característica por apresentarem poucos pokémon no geral. Assim, é necessário menos pokémon poderosos para influenciar drasticamente na média dessas gerações.")

tiposelec = st.selectbox('Escolha o tipo ou geração a ser analizado!', ['Todos', 'Water', 'Fire','Grass',
'Electric','Ghost','Normal','Psychic','Rock','Flying','Ground',
'Bug','Dragon','Dark','Fighting','Ice','Poison','Steel','Fairy',"1ª Geração","2ª Geração","3ª Geração",
"4ª Geração","5ª Geração","6ª Geração","7ª Geração"
,"8ª Geração","9ª Geração"])

tipo_escolhido = tiposelec

#============================= Função para achar o maior atributo médio para cada tipo, declarada para possíveis automatizações =================================

def media_maior(tipo):
    if tipo == tipo_escolhido:
        dic_maior_media_cada_tipo = {}

        for nome, tipo in dic_nome_tipo.items():

            dic_maior_media_cada_tipo[nome] =  tipo[atributos].mean().max()

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

            st.write(f"O atributo com maior média dos pokémon {nome} é {nome_maior} com {maior:.2f}")

        dic_maior_media_cada_tipo[nome] = [nome_maior, tipo[atributos].mean().max()]

#==================================================================================================================================================


st.subheader("Média dos atributos da opção selecionada: ")

for k, v in dic_nome_tipo.items():
    if k == tipo_escolhido:
        for atributo in atributos:
            st.write(f"{atributo}: " f"{v[atributo].mean():.2f}")


# Dicionário com cores para cada tipo ou geração
cores_tipo = {
    "Todos": "lavender",
    "Water": "blue", 
    "Fire": "red", 
    "Grass": "green", 
    "Electric": "yellow", 
    "Ghost": "mediumpurple", 
    "Normal": "silver", 
    "Psychic": "hotpink", 
    "Rock": "gray", 
    "Flying": "lightcyan", 
    "Bug": "springgreen", 
    "Ground": "burlywood", 
    "Dragon": "royalblue", 
    "Dark": "black", 
    "Fighting": "firebrick", 
    "Ice": "deepskyblue", 
    "Poison": "blueviolet", 
    "Steel": "slategrey", 
    "Fairy": "lightpink", 
    "1ª Geração": "red", 
    "2ª Geração": "gold", 
    "3ª Geração": "lime", 
    "4ª Geração": "lightcyan", 
    "5ª Geração": "grey", 
    "6ª Geração": "mediumblue", 
    "7ª Geração": "orange", 
    "8ª Geração": "aqua", 
    "9ª Geração": "darkviolet"
}

# Depois de calcular e exibir a média dos atributos
if tiposelec:
    tipo_escolhido = tiposelec

    # Inicializando a lista para armazenar as médias dos atributos
    media_atributos = []
    for k, v in dic_nome_tipo.items():
        if k == tipo_escolhido:
            # Calculando a média de cada atributo para o tipo selecionado
            for atributo in atributos:
                media_atributos.append(v[atributo].mean())
    
    # Cor do gráfico com base no tipo selecionado
    cor_do_tipo = cores_tipo.get(tipo_escolhido, "gray")  # Padrão "gray" se não encontrar o tipo
    
    # Criando o gráfico de barras com as médias dos atributos
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_ylim(0,110)
    ax.bar(atributos, media_atributos, color=cor_do_tipo, edgecolor="black")
    ax.set_xlabel("Atributos")
    ax.set_ylabel("Valor Médio")
    ax.set_title(f"Média dos Atributos de {tipo_escolhido}")
    st.pyplot(fig)


st.subheader ("Pokemon mais fraco em cada atributo:")

if tiposelec:
  nome_min_atributos_pokedex = []
  img_min_atributos_pokedex = []

  for k, v in dic_nome_tipo.items():
   if k == tipo_escolhido:
      i = 0
      for atributo in atributos:
        nome_min_atributos_pokedex.append(v[v[atributo] == v[atributo].min()]["Name"].values[0])
        img_min_atributos_pokedex.append(v[v[atributo] == v[atributo].min()]["Image"].values[0])
        st.write("Com " f"{v[atributo].max()}" " de " f"{atributo}: "f"{nome_min_atributos_pokedex[atributos.index(atributo)]}")
        print(nome_min_atributos_pokedex)
        printar_imagem(img_min_atributos_pokedex[atributos.index(atributo)])
        st.markdown('##')



st.subheader ("Pokémon mais forte em cada atributo:")

if tiposelec:

  nome_min_atributos_pokedex = []
  img_min_atributos_pokedex = []

  for k, v in dic_nome_tipo.items():
   if k == tipo_escolhido:
      for atributo in atributos:
        nome_min_atributos_pokedex.append(v[v[atributo] == v[atributo].max()]["Name"].values[0])
        img_min_atributos_pokedex.append(v[v[atributo] == v[atributo].max()]["Image"].values[0])
        st.write("Com " f"{v[atributo].max()}" " de " f"{atributo}: "f"{nome_min_atributos_pokedex[atributos.index(atributo)]}")
        print(nome_min_atributos_pokedex)
        printar_imagem(img_min_atributos_pokedex[atributos.index(atributo)])
        st.markdown('##')

st.subheader ("Extra: Pokémon favoritos de cada integrante do grupo")

st.write("Arthur Faria: Joltik")
st.image("images/720.png", caption=" ", width=200, use_container_width=False)

st.write("Alexandre RIbeiro: Snorunt")
st.image("images/445.png", caption=" ", width=200, use_container_width=False)

st.write("Eduardo Tavares: Metagross")
st.image("images/462.png", caption=" ", width=200, use_container_width=False)

st.write("Moises Auad: Feraligatr")
st.image("images/214.png", caption=" ", width=200, use_container_width=False)

st.write("Victor Hugo Ribeiro: Gardevoir")
st.image("images/352.png", caption=" ", width=200, use_container_width=False)