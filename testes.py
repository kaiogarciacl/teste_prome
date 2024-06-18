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

    rows = f""" select * from [3_tabela_comandos] """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        rows = f""" {row[0]} """
        cursor = cn.conexao_sql.cursor()
        cursor.execute(rows)
        rows = cursor.fetchall()
        for row in rows:
            st.markdown(row[0])
