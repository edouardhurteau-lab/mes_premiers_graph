import streamlit as st
import pandas as pd
import altair as alt

st.title("Mes premiers graphiques")

titanic=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv", sep = ',')  # liste des df.
tips=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/tips.csv", sep = ',')
penguins=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv", sep = ',')

base = st.selectbox("Choisis une base de donnée",['titanic', 'tips', 'penguins']) # choix de la base du df

if base == 'titanic':
    df=titanic
elif base == 'tips':
    df=tips
else :
    df=penguins
st.subheader("Voici un extrait de la base")
st.dataframe(df.head(10))

liste_x=list(df.columns)        # je fais une liste de la colonne

st.title("Choisis les deux valeurs de ton graphique")  # je definis x et y
valeur_x=st.selectbox("Choisis la valeur de l'axe X",liste_x)
liste_y = liste_x.copy()
liste_y.remove(valeur_x)
valeur_y=st.selectbox("Choisis la valeur de l'axe Y", liste_y)

graph=st.selectbox( "choisis un graphique",["nuage de points","graphique en barre","ligne graphique"]) # choix du graph

df_plot = df[[valeur_x, valeur_y]].dropna() # on retire les Nan

# --- Détection du type de données ---
x_type = 'quantitative' if pd.api.types.is_numeric_dtype(df_plot[valeur_x]) else 'nominal'  # differencier les type num et str
y_type = 'quantitative' if pd.api.types.is_numeric_dtype(df_plot[valeur_y]) else 'nominal'


# --- Création du graphique avec Altair ---
if graph == "nuage de points":
    chart = alt.Chart(df_plot).mark_point().encode(
        x=alt.X(valeur_x, type=x_type),
        y=alt.Y(valeur_y, type=y_type),
        tooltip=[valeur_x, valeur_y]  # affiche les valeurs au survol
    ).interactive()  # permet zoom/pan
    st.altair_chart(chart, use_container_width=True)

elif graph == "graphique en barre":
    chart = alt.Chart(df_plot).mark_bar().encode(
        x=alt.X(valeur_x, type=x_type),
        y=alt.Y(valeur_y, type=y_type),
        tooltip=[valeur_x, valeur_y]
    )
    st.altair_chart(chart, use_container_width=True)

elif graph == "ligne graphique":
    chart = alt.Chart(df_plot).mark_line().encode(
        x=alt.X(valeur_x, type=x_type),
        y=alt.Y(valeur_y, type=y_type),
        tooltip=[valeur_x, valeur_y]
    )
    st.altair_chart(chart, use_container_width=True)