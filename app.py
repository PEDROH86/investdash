#   py -m streamlit run "c:/Users/Pedro/Meu Drive/dev/APP03/app.py"
import streamlit as st
#from streamlit_option_menu import option_menu
from __init__ import option_menu

st.set_page_config(page_title= 'DashFin 1.0', layout='wide')

from tkinter import *
import defyfinance as yf

from carteiraFiis import *
from carteiraAcoes import *
from carteiraStocks import *
from ir import *
selected = option_menu(
    menu_title=None,
    options=['DashBoard', 'Carteira FIIs', 'Carteira Ações', 'Carteira Stocks', 'IR'],
    default_index=0,
    orientation='horizontal',
    #styles=
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if selected == 'Carteira FIIs':
    carteira_fiis()
if selected == 'Carteira Ações':
    carteira_acoes()
if selected == 'Carteira Stocks':
    carteira_stocks()
if selected == 'IR':
    ir()

if selected == 'DashBoard':
    st.header('DeashBoard Fin 1.0')
    ticker = ''
    st.header('Digite o Ticker')
    ticker = st.text_input(label='Ex. VALE3').strip().upper()
    bt = st.button('ok')
    if ticker or bt:
        st.text(str(yf.nome(ticker)).capitalize())
        moeda = str(yf.moeda(ticker))
        valor = f'{yf.cotacao(ticker):.2f}'
        st.text(moeda + ' ' + valor)
    else:
        ticker = ''
