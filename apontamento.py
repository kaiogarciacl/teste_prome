import streamlit as st
import conexao as cn
import models
from streamlit_modal import Modal


def apontamento():
    colb1, colb2, colb3 = st.columns([2.4, 3, 1])
    with colb2:
        st.image(fr'D:\img_prometheus\prometeus_sem_fundo.jpg', width=400)
    cold1, cold2, cold3 = st.columns([2.35, 3, 1])
    with cold2:
        st.title('Apontamento de Atividade')

    cola1, cola2, cola3 = st.columns([2.7, 2, 2.7])
    with cola2:
        colb1, colb2 = st.columns(2)
        with colb1:
            cracha = st.text_input('Crácha', key='cracha', max_chars=8)
        with colb2:
            atv = st.text_input('Atividade', key='Atividade')

            def limpa_tudo():
                st.session_state['cracha'] = ''
                st.session_state['Atividade'] = ''

            def limpa_atv():
                st.session_state['Atividade'] = ''

        cola1, cola2 = st.columns([0.5, 2])
        with cola2:
            if cracha == '' and atv == '':
                st.subheader(':blue[↖ Escanear seu Crachá]')
            if cracha != '' and atv == '':
                st.subheader(':blue[Escanear sua Atividade ↗]')
            if cracha == '' and atv != '':
                st.subheader(':blue[↖ Escanear seu Crachá]')
        if cracha != '' and atv != '':
            rows = f""" if exists (select cracha from colaboradores where cracha = '{cracha}') BEGIN select 'CONSTA' END ELSE  select 'NÃO CONSTA'  """
            cursor = cn.conexao_sql.cursor()
            cursor.execute(rows)
            rows = cursor.fetchall()
            for row in rows:
                verifica_colaborador = row[0]
                if verifica_colaborador == 'NÃO CONSTA':
                    st.subheader(f""":red[Colaborador Não Cadastrado]""")

                if verifica_colaborador == 'CONSTA':
                    rows = f""" select * from colaboradores where cracha = '{cracha}'  """
                    cursor = cn.conexao_sql.cursor()
                    cursor.execute(rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        st.subheader(f"""Colaborador: :blue[{row[0]}]""")

            st.markdown('______________________________')
    cola1, cola2, cola3 = st.columns([2, 3, 2])
    with cola2:
        if cracha != '' and atv != '' and verifica_colaborador == 'CONSTA':
            if verifica_colaborador == 'CONSTA':
                rows = f""" if exists (select cod_barra_novo from apontamento2 where cod_barra_novo = '{atv}') BEGIN select 'CONSTA' END ELSE  select 'NÃO CONSTA'  """
                cursor = cn.conexao_sql.cursor()
                cursor.execute(rows)
                rows = cursor.fetchall()
                for row in rows:
                    verifica_atvidade = row[0]

            if verifica_colaborador == 'CONSTA' and verifica_atvidade == 'NÃO CONSTA':
                st.subheader(f""":red[Atividade Não Registrada]""")

            else:
                rows = f""" select * from apontamento2 where cod_barra_novo = '{atv}' """
                cursor = cn.conexao_sql.cursor()
                cursor.execute(rows)
                rows = cursor.fetchall()
                for row in rows:
                    id_apontamento2 = row[0]
                op = atv.split('-')[0]
                rows = f""" select chav, id, pv, cliente, pedcliente, cod, descricao, qtd, saldo, caminho, caminhoimg, ppcid, opid, idpesquisa, revproce from carteira where op = '{op}'  """
                cursor = cn.conexao_sql.cursor()
                cursor.execute(rows)
                rows = cursor.fetchall()
                for row in rows:

                    st.header(f'Informações da OP: :blue[{op}]')
                    st.subheader(f'Cliente: :blue[{row[3]}]')
                    st.subheader(f'Código: :blue[{row[5]}] Rev. :blue[{row[14]}]')
                    st.subheader(f'Descrição: :blue[{row[6]}]')

                    rows = f""" if exists (select cod_barra_novo from apontamento2 where cod_barra_novo = '{atv}' and avt_status = 'AF') BEGIN select 'CONSTA' END ELSE  select 'NÃO CONSTA'  """
                    cursor = cn.conexao_sql.cursor()
                    cursor.execute(rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        verifica_apontamento2 = row[0]

                        if verifica_apontamento2 == 'CONSTA':
                            rows = f""" if exists (select ids from apontamento where atvs = '{atv}' and motfims = 'Finalizado') BEGIN select 'CONSTA' END ELSE  select 'NÃO CONSTA'  """
                            cursor = cn.conexao_sql.cursor()
                            cursor.execute(rows)
                            rows = cursor.fetchall()
                            for row in rows:
                                tem_apontamento = row[0]

                                if tem_apontamento == 'CONSTA':
                                    rows = f""" select * from apontamento where atvs = '{atv}' and motfims = 'Finalizado'  """
                                    cursor = cn.conexao_sql.cursor()
                                    cursor.execute(rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        cracha_que_terminou = row[1]
                                        rows = f""" select * from colaboradores where cracha = '{cracha_que_terminou}'"""
                                        cursor = cn.conexao_sql.cursor()
                                        cursor.execute(rows)
                                        rows = cursor.fetchall()
                                        for row in rows:
                                            st.info(f'**Atenção Esta Atividade foi Finalizada por: :red[{row[0]}]**')
                                else:
                                    st.info(f'**Atenção Esta Atividade foi Finalizada**')

                            senha_lider = st.text_input('Senha de Liberação do Lider', type='password')
                            if senha_lider != '':
                                if senha_lider == '742596':
                                    iniciar = st.button('Abrir Retrabalho', key='Retrabalho', use_container_width=True)
                                    if iniciar:
                                        models.comando = f""" update apontamento2 set avt_status = case when id = '{id_apontamento2}' then 'ANF' else avt_status end """
                                        cn.ins_upd_del()

                                else:
                                    st.info('**:red[Senha Incoreta]**')
                                    iniciar = st.button('Abrir Retrabalho', key='Retrabalho', use_container_width=True, disabled=True)
                            else:
                                iniciar = st.button('Abrir Retrabalho', key='Retrabalho', use_container_width=True, disabled=True)
                        if verifica_apontamento2 == 'NÃO CONSTA':
                            rows = f""" if exists (select atvs from apontamento where atvs = '{atv}' and motfims = 'Processando') BEGIN select 'CONSTA' END ELSE  select 'NÃO CONSTA'  """
                            cursor = cn.conexao_sql.cursor()
                            cursor.execute(rows)
                            rows = cursor.fetchall()
                            for row in rows:
                                verifica_aberto = row[0]
                                if verifica_aberto == 'CONSTA':
                                    rows = f""" select * from apontamento where atvs = '{atv}' and motfims = 'Processando' """
                                    cursor = cn.conexao_sql.cursor()
                                    cursor.execute(rows)
                                    rows = cursor.fetchall()
                                    for row in rows:
                                        cracha_que_ta_aberto = row[1]
                                        rows = f""" select * from colaboradores where cracha = '{cracha_que_ta_aberto}'"""
                                        cursor = cn.conexao_sql.cursor()
                                        cursor.execute(rows)
                                        rows = cursor.fetchall()
                                        for row in rows:
                                            st.info(f'**Atenção Esta Aberta com o Colaborador: :red[{row[0]}]**')

                                    senha_lider = st.text_input('Senha de Liberação do Lider', type='password')
                                    if senha_lider != '':
                                        if senha_lider == '742596':
                                            iniciar = st.button('Abrir Atividade de Apoio', key='Retrabalho', use_container_width=True)
                                            if iniciar:
                                                st.markdown('iniciar apoio')
                                        else:
                                            st.info('**:red[Senha Incoreta]**')
                                            iniciar = st.button('Abrir Atividade de Apoio', key='Retrabalho', use_container_width=True, disabled=True)
                                    else:
                                        iniciar = st.button('Abrir Atividade de Apoio', key='Retrabalho',
                                                            use_container_width=True, disabled=True)
                                else:
                                    iniciar = st.button('Iniciar Atividade', key='Retrabalho', use_container_width=True)

    if cracha != '' and atv != '' and verifica_colaborador == 'CONSTA':
        if iniciar:
            modal = Modal("Deseja Abir Outra Atividade", key="demo-modal", padding=20, max_width=500)
            with modal.container():
                colp1, colp2 = st.columns(2)
                with colp1:
                    sim = st.button('**:green[SIM]**', use_container_width=True, on_click=limpa_atv, key='sim')
                with colp2:
                    nao = st.button('**:red[Não]**', use_container_width=True, on_click=limpa_tudo, key='nao')



    st.title('')



