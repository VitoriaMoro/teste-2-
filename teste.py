import streamlit as st
import pandas as pd 
import numpy as np 

st.write("""
# My first app
Hello *world!*
""")
st.text_input("Digite seu nome:")
st.text_input("Digite o seu sobrenome:")
st.text_input("Digite a sua idade:")
st.text_input("Digite o seu email:")
st.text_input("Digite o seu CPF:")
st.write("Seu cadastro esta completo, clique no botão abaixo para avançar!")
