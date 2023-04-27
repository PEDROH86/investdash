import streamlit as st
import defyfinance as yf
from tkinter import *

def carteira_fiis():
    st.header('Carteira FIIs Page')
    bt2 = st.button('Gerenciar ativos')
    if bt2:
        janela_pop()

def janela_pop():
    janela = Tk()
    janela.title('Lançar Ativos')
    titulo = Label(janela, text='Insira um ativo na carteira:')
    titulo.grid(column=0, row=0)

    janela.mainloop()
