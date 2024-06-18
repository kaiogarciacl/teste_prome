import streamlit as st
import hydralit_components as hc
from streamlit_modal import Modal
import testes


st.set_page_config(page_title="PROMETHEUS",layout="wide", initial_sidebar_state="collapsed")

with open("style.css") as f:st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with st.sidebar:
    
    log = st.text_input('LOG', label_visibility='collapsed', placeholder='Login', key='Log')
    senha = st.text_input('senha', label_visibility='collapsed', placeholder='Senha', key='senha', type='password')

if log != '' and senha != '' :
    menu_opcao = [
    
        {'icon': 'bi bi-bar-chart', 'label': 'Indicadores'},
    
        {'icon': 'bi bi-person-circle', 'label': 'Conta',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Ponto'},
                     {'icon': 'bi bi-person-plus', 'label': 'Configuração da Conta'}]},
    
        {'icon': 'bi bi-person-circle', 'label': 'Teste'}]

    
    tema = {'txc_inactive': 'black', 'menu_background': '#eaeaea', 'txc_active': 'black', 'option_active': '#ffffff', 'gap': '0rem'}
    opcao = hc.nav_bar(menu_definition=menu_opcao, home_name='Ambiente', override_theme=tema, sticky_mode='sticky', sticky_nav=False)

    if opcao == 'Teste':
        testes.teste()
