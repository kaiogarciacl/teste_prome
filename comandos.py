import conexao
import models as md
import conexao as cn
import time
import streamlit as st


def atualizar_nest_plano():
    md.comando = f""" update cortelaser set Plano = case when id = '{md.id_alter}' then '{md.plano_novo}' else Plano end """
    cn.ins_upd_del()


def reservar_sala():
    md.comando = f""" insert into [2_tabela_reserva_sala_reu] (colaborador, dia, hora_ini, hora_fim, motivo)
                    values ('{md.usuario}', '{md.dia}', '{md.h_ini}', '{md.h_fim}', '{md.motivo}')"""
    cn.ins_upd_del()


def excluir_horaio_sala_reuniao():
    md.comando = f""" delete [2_tabela_reserva_sala_reu] where id = '{md.id_excluir_reuniao}' """
    cn.ins_upd_del()


def fecha_pop_up_sala_reuniao():
    md.comando = f""" update login set id_pop_up_sala = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def abri_pop_up_sala_mo_falha():
    md.comando = f""" update login set pop_up_modo_falha = 'Sim' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def fecha_pop_up_sala_mo_falha():
    md.comando = f""" update login set pop_up_modo_falha = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def add_falha():
    md.comando = f""" insert into [2_tabela_cod_falhas] (cod_falha, criado_por) values ('{md.mod_falha}', '{md.usuario}') """
    cn.ins_upd_del()


def abri_pop_up_fallow():
    md.comando = f""" update login set pop_up_fallow_up = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_pop_up_fallow():
    md.comando = f""" update login set pop_up_fallow_up = '', op_pop_up_fallow_up = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def abri_pop_reuniao():
    md.comando = f""" update login set id_pop_up_sala = 'Sim' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def add_atv_fallow():
    md.comando = f""" insert into [2_tabela_follow up] (cod, cliente, descricao, responsavel, dt_limite, info, dt_lancado, finalizado, dt_finalizado, op_ref, indicar_termino, motivo_canel_usuario, pop_aberto)
                        values ('{md.cod_f}', '{md.cliente_f}', '{md.decri_f}', '{md.resp_f}', '{md.dt_f}', '{md.det_atv_f}', GETDATE(), 'N', '', '{md.op_f}', 'N', 'Nada Declarado', '') """
    cn.ins_upd_del()


def alter_data_fallow():
    md.comando = f""" insert into diario( op, motcancelar, diario, setor, data, usuario) values ('{md.op_f}', '{md.det_cancel_atv_f}', 'Prolongamento de Data', 'Fallow UP', GETDATE(), '{md.usuario}') 
                      update [2_tabela_follow up] set dt_limite = '{md.data_prolonga_fallow}' where id = '{md.id_prolonga_fallow}'  """
    cn.ins_upd_del()


def fecahr_pop_up_troca_data():
    md.comando = f""" update login set tem_pop_up_porlonga = '', id_pop_up_prolonga_fallow = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def abri_pop_up_pendencia():
    md.comando = f""" update login set pop_up_atv_pendencia = 'S' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def fechar_pop_up_pendencia():
    md.comando = f""" update login set pop_up_atv_pendencia = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def fecha_pendencia():
    md.comando = f""" update [2_tabela_follow up] set motivo_canel_usuario = '{md.obs_fecha_pendencia}' , indicar_termino = 'S' , dt_indicado = GETDATE() where id = '{md.id_tela_pendencia}' """
    cn.ins_upd_del()


def recaregar():
    md.comando = f""" update login set id_pop_up_prolonga_fallow = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()

def cria_tesdte():
    md.comando = f""" insert into [2_tabela_cadastros_componentes]
                         (cliente, id_chave, cod_componente_cliente, rev_componente, descri_componente, qtd_componente, material_interno, largura, dt_lancado, cod_interno, rev_interno,  descricao_interna, saldo, usuario, tipo_op, comprimento, peso)
                        values('{md.f_cliente}', '{md.id_chave_componente}', '{md.cod_com}', '{md.rev_com}', '{md.des_com}', '{md.qtd_com}', '{md.mp_com}', '{md.dimen_com}', GETDATE(), '', '0', '{md.des_com}', '{md.qtd_com}', '{md.usuario}', 'Componente', '0', '0') """
    cn.ins_upd_del()


def salva_componente_cria_op():
    md.comando = f""" update [2_tabela_cadastros_componentes] set cod_componente_cliente = '{md.cod_com}', rev_componente = '{md.rev_com}',
    descri_componente = '{md.des_com}', qtd_componente = '{md.qtd_com}', material_interno = '{md.mp_com}',
    largura = '{md.dimen_lar}', comprimento = '{md.dimen_com}', peso = '{md.peso}' where id = '{md.id_excluir_agora}' """
    cn.ins_upd_del()


def update_componente():
    md.comando = f""" insert into [2_tabela_cadastros_componentes]
                         (cliente, id_chave, cod_componente_cliente, rev_componente, descri_componente, qtd_componente, material_interno, largura, dt_lancado, cod_interno, saldo, usuario, comprimento, peso, tipo_op, area)
                        values('{md.f_cliente}', '{md.id_chave_componente}', '{md.cod_com}', '{md.rev_com}', '{md.des_com}', '{md.qtd_com}', '{md.mp_com}', '{md.dimen_lar}', GETDATE(), '', {md.qtd_com}, '{md.usuario}', '{md.dimen_com}', '{md.peso}', 'Componente', '{md.area_cad}') """
    cn.ins_upd_del()



def abri_pop_up_cad_componente():
    md.comando = f""" update login set pop_up_cad_component = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def abri_pop_up_cad_componente_agrupa():
    md.comando = f""" update login set pop_up_cad_component = 'Simm' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_pop_up_cad_componente():
    md.comando = f""" update login set pop_up_cad_component = '', id_pop_up_cad_component = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def salva_componente_cria_op_2():
    md.comando = f""" insert into [2_tabela_cadastros_componentes]
                     (cliente, id_chave, cod_componente_cliente, rev_componente, descri_componente, qtd_componente, material_interno, largura, dt_lancado, cod_interno, rev_interno,  descricao_interna, saldo, usuario, tipo_op, comprimento, peso)
                    values('{md.f_cliente}', '{md.id_chave_componente}', '{md.cod_com}', '{md.rev_com}', '{md.des_com}', '{md.qtd_com}', '{md.mp_com}', '{md.dimen_com}', GETDATE(), '', '0', '{md.des_com}', '{md.qtd_com}', '{md.usuario}', 'Filho', '0', '0') """
    cn.ins_upd_del()


def cad_item_pedido():
    md.comando = f""" insert into [1_tabela_pedido] (id_ped, cliente, part_number, rev_cliente, descricao, qtd, peso, dt_recebido, dt_entrega, dt_lancado, usuario, pop_up_finalizado, dt_finalizado_lista, valor)
                        values ('{md.id_ped_orca}', '{md.cliente_ped_orca}', '{md.cod_ped_orca}', '{md.rev_ped_orca}', '{md.descricao_ped_orca}', '{md.demanda_ped_orca}', '{md.peso_ped_orca}', '{md.dt_recebido_ped_orca}', '{md.dt_entrega_ped_orca}', GETDATE(), '{md.usuario}', 'Não', '', '{md.valor_ped_orca}') 
                        update login set pop_up_check_list = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_cad_item_pedido():
    md.comando = f""" update login set pop_up_check_list = '', id_pop_up_check_list = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def rev_check():
    md.comando = f""" update login set pop_up_check_list = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def abri_pop_up_metodos():
    md.comando = f""" update login set pop_up_temp_metodo = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_pop_up_metodos():
    md.comando = f""" update login set pop_up_temp_metodo = '', id_pop_up_temp_metodo = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def abri_pop_up_fim_orcamento():
    md.comando = f""" update login set pop_up_finalizar_orcamento = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_pop_up_fim_orcamento():
    md.comando = f""" update login set pop_up_finalizar_orcamento = '', id_pop_up_finalizar_orcamento = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def finalizar_orcamento():
    rows = f""" select id_para_finalizar_orcamento, valor_para_fechar_orcamento from login where nome = '{md.usuario}'  """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        id_fecha = row[0]
        valor_orcamento = row[1]
    md.comando = f""" update [1_tabela_pedido] set valor = '{valor_orcamento}', dt_finalizado_lista = GETDATE() where id = '{id_fecha}' 
                              update login set id_para_finalizar_orcamento = '0', valor_para_fechar_orcamento = '0' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def finalizar_orcamento2():
    rows = f""" select id_para_finalizar_orcamento, valor_para_fechar_orcamento from login where nome = '{md.usuario}'  """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        id_fecha = row[0]
    md.comando = f""" update [1_tabela_pedido] set valor = '0', dt_finalizado_lista = '1900-01-01 00:00:00.000' where id = '{id_fecha}'
                              update login set id_para_finalizar_orcamento = '0', valor_para_fechar_orcamento = '0' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def abrir_fechar_pedido():
    md.comando = f""" update login set pop_up_finalizar_pedido = 'Sim' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fechar_fechar_pedido():
    md.comando = f""" update login set id_pop_up_finalizar_pedido = '', pop_up_finalizar_pedido = '', tipo_pop_up = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def abrir_i_frame():
    md.comando = f""" update login set i_frame_aberto = '{md.i_frame}' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def fecha_i_frame():
    md.comando = f""" update login set i_frame_aberto = '' where nome = '{md.usuario}'"""
    cn.ins_upd_del()


def excluir_lista_elementos():
    rows = f""" if exists (select id from [2_tabela_cadastros_filhos] where excluir = 'Sim') BEGIN select id, id_chave_devolver, qtd from [2_tabela_cadastros_filhos] where excluir = 'Sim' END ELSE  select 'NÃO CONSTA' """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        if row[0] != 'NÃO CONSTA':
            md.comando = f""" update [2_tabela_cadastros_componentes] set saldo = saldo + {row[2]} where id = '{row[1]}'
                                   delete [2_tabela_cadastros_filhos] where id = {row[0]} """
            cn.ins_upd_del()


def fecha_pop_up_sci():
    md.comando = f""" update login set id_pop_up_sci = '', pop_up_sci = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def fecha_pop_up_tempos_metodos():
    md.comando = f""" update login set id_pop_up_tempos_geral = '', pop_up_tempos_geral = '' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def salvar_laser():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, total_furos, perimetro, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.perimetro_laser}', '{md.n_pircing}', 'Cortar') """
    cn.ins_upd_del()


def excluir_tempo():
    md.comando = f""" delete [1_tabela_tempos] where excluir = 'Sim' """
    cn.ins_upd_del()


def salvar_serra():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, maior_med_serra, menor_med_serra, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.maior_med_serra}', '{md.menor_med_serr}', 'Cortar') """
    cn.ins_upd_del()


def salvar_dobra():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, total_de_dobra, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.total_dobra}', 'Dobrar') """
    cn.ins_upd_del()


def salvar_usinagem():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, dn_ini_usi, dn_fim_usi, compri_usi, nivel_usi, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.dn_maior_usg}', '{md.dn_menor_usg}', '{md.comprimento_usg}', '{md.nivel_usg}', '{md.atv}') """
    cn.ins_upd_del()


def salvar_usinagem_rosca():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, qual_rosca, passe_rosca, compri_usi, nivel_usi, atividade, rep_furo)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.qual_rosca}', '{md.passe_rosca}', '{md.comprimento_usg}', '{md.nivel_usg}', '{md.atv}', '{md.rep_furo}') """
    cn.ins_upd_del()


def salvar_usinagem_furo():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade, pre_furo, dn_furo, comprimento_furo, rep_furo)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.atv}', '{md.pre_furo}', '{md.dn_furo}', '{md.comprimento_furo}', '{md.rep_furo}') """
    cn.ins_upd_del()


def fecha_histo():
    md.comando = f""" update reqlaser set ver_hiso = '' where ver_hiso = 'Sim' """
    cn.ins_upd_del()


def fecha_histo2():
    md.comando = f""" update reqlaser set ta_aberto = '' where ta_aberto = 'Sim' """
    cn.ins_upd_del()


def salvar_solda():
    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade, perna, perimetro_solda, qtd_vez_solda)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', 'Soldar', '{md.perna}', '{md.perimetro_solda}', '{md.qtd_vez_solda}') """
    cn.ins_upd_del()


def salvar_fresa():

    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade, altura_ini_fresa, altura_fim_fresa, comprimento_fresa, largura_fresa)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.atv}', '{md.altura_ini_fresa}', '{md.altura_fim_fresa}', '{md.comprimento_fresa}', '{md.largura_fresa}') """
    cn.ins_upd_del()

def salvar_montagem():

    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.recurso}') """
    cn.ins_upd_del()


def proxi_pag():

    rows = f""" select id_pop_up_cad_component from login where nome = '{md.usuario}' """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        id_aberto_pula = row[0]

    rows = f""" select top 1 id from [2_tabela_cadastros_componentes] where id_chave = '{md.id_alter_pr}' and id > '{id_aberto_pula}' """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        resultado = row[0]

    md.comando = f""" update login set id_pop_up_cad_component = '{resultado}', pop_up_cad_component = 'Sim' where nome = '{md.usuario}' """
    cn.ins_upd_del()


def voltar_pag():

    rows = f""" select id_pop_up_cad_component from login where nome = '{md.usuario}' """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        id_aberto_pula = row[0]

    rows = f""" select top 1 id from [2_tabela_cadastros_componentes] where id_chave = '{md.id_alter_pr}' and id < '{id_aberto_pula}' order by id desc """
    cursor = cn.conexao_sql.cursor()
    cursor.execute(rows)
    rows = cursor.fetchall()
    for row in rows:
        resultado = row[0]

    md.comando = f""" update login set id_pop_up_cad_component = '{resultado}', pop_up_cad_component = 'Sim' where nome = '{md.usuario}' """
    cn.ins_upd_del()



def salvar_qualidade():

    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade)
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.atv}') """
    cn.ins_upd_del()


def salvar_jato():

    md.comando = f""" insert into [1_tabela_tempos] (usuario, dt_lancado, id_chave, id_id_chave, cod, recurso, tempo_minuto, atividade, total_tinta, area_jato )
    values ('{md.usuario}', GETDATE(), '{md.id_chave_salva}', '{md.id_id_chave_salva}', '{md.cod_tempo}', '{md.recurso}', '{md.tempo_minuto}', '{md.recurso}', '{md.area_jato}', '{md.total_tinta}') """
    cn.ins_upd_del()


def ta_liberado():
    st.toast('Caregando')


def vai_porra():
    md.comando = f""" insert into [3_tabela_comandos] (comando, status, hora)
        values ('{md.executar}', '', GETDATE()) 
        
        """
    cn.ins_upd_del()









