import pyodbc as py
import models as md
import time



rows = f""" SELECT case when count(command)  = '1' then 'Liberado' else 'Esperar' end FROM sys.dm_exec_requests r CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t """
cursor = py.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=PC-13; DATABASE=Base_cl; UID=sa; PWD=').cursor()
cursor.execute(rows)
rows = cursor.fetchall()
for row in rows:
    if row[0] == 'Liberado':
        md.liberador_excucao = 'Liberadao'
        conexao_sql = py.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=PC-13; DATABASE=Base_cl; UID=sa; PWD=')
    else:
        md.liberador_excucao = 'Não Liberado'
        time.sleep(0.15)
        conexao_sql = py.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=PC-13; DATABASE=Base_cl; UID=sa; PWD=')
        espera = "BEGIN WAITFOR DELAY '00:00:04';"


def pesquisar_tabela(query):
    rows = f""" SELECT count(command) FROM sys.dm_exec_requests r CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t """
    cursor = conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        if int(row[0]) == 1:
            with conexao_sql.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()
        else:
            time.sleep(0.2)
            with conexao_sql.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()

def ins_upd_del():
    conexao_sql.cursor()
    conexao_sql.execute(f'{md.comando}')
    conexao_sql.commit()











