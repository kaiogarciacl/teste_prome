import streamlit as st

from streamlit_modal import Modal
import testes
import models as md
import comandos


st.set_page_config(page_title="PROMETHEUS",layout="wide", initial_sidebar_state="collapsed")

with open("style.css") as f:st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


with st.sidebar:
    
    log = st.text_input('LOG', label_visibility='collapsed', placeholder='Login', key='Log')
    senha = st.text_input('senha', label_visibility='collapsed', placeholder='Senha', key='senha', type='password')

if log != '' and senha != '' : 
    comando = st.text_area('comando')

    def vai():
        md.executar = comando
        comandos.vai_porra()
        
    st.button('vai', on_click=vai)
