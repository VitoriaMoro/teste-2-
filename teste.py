import streamlit as st
import pandas as pd 
import numpy as np 

st.write("""
# My first app
Realize o seu cadastro para participar de futuras pesquisas da FGV Rio!*
""")
st.text_input("Digite seu nome:")
st.text_input("Digite o seu sobrenome:")
st.text_input("Digite a sua idade:")
st.text_input("Digite o seu email:")
st.text_input("Digite o seu CPF:")
st.write("Após responder todas as perguntas, seu cadastro estará completo. Clique no botão abaixo para avançar!")
st.button("AVANÇAR")
