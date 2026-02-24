# Pacote de implementação da máquina preditiva
import streamlit as st

# Kit de ferramenta do processamento de linguagem natural
import nltk

# Titulo do Sistema  Streamlit
st.write("Pesquisa de satisfação do cliente")

# Entradas de dados com manifestação do cliente
user_input = st.text_input("Como foi seu atendimento: ")

# Máquina preditiva de sastifação do cliente
# Baixar o dicionário do VADER
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

if user_input:
    # Polaritu_score retorna o sentimento que usuário: negativa ou positiva
    score = sia.polarity_scores(user_input)

    if score["neg"] != 0:
        st.write("Análise Negativa 😊")

    elif score["pos"] != 0:
        st.write("Análise Positiva 😡")

    else:
        st.write("Análise Neutra 😐")