import streamlit as st
import comandos
import conexao as cn
import models as md

def teste():
    comando = st.text_area('comando')

    def vai():
        md.executar = comando
        comandos.vai_porra()
        
    st.button('vai', on_click=vai)
