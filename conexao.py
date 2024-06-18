import pyodbc as py
import streamlit as st
import streamlit.components.v1 as components
import comandos
import models as md
import time



@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
        + st.secrets["server"]
        + ";DATABASE="
        + st.secrets["database"]
        + ";UID="
        + st.secrets["username"]
        + ";PWD="
        + st.secrets["password"]
    )

conexao_sql = init_connection()


def pesquisar_tabela(query):
    with conexao_sql.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()


def ins_upd_del():
    conexao_sql.cursor()
    conexao_sql.execute(f'{md.comando}')
    conexao_sql.commit()











