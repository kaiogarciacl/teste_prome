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
        {'icon': 'bi bi-building', 'label': 'Comercial',
         'submenu': [{'icon': 'bi bi-list-ol', 'label': 'Abrir Orçamento'},
                     {'icon': 'bi bi-inboxes-fill', 'label': 'Finalizar Orçamento'},
                     {'icon': 'bi bi-cash-coin', 'label': 'Precificação'},
                     {'icon': 'bi bi-bag-check', 'label': 'Aprovação'}]},
    
        {'icon': 'bi bi-gear-wide-connected', 'label': 'Engenharia',
         'submenu': [{'icon': 'bi bi-arrow-repeat', 'label': 'Atualizar Códigos'},
                     {'icon': 'bi bi-list-ol', 'label': 'Análise Crítica'},
                     {'icon': 'bi bi-clock-history', 'label': 'Tempos e Métodos'}]},
    
        {'icon': 'bi bi-list-columns-reverse', 'label': 'PCP',
         'submenu': [{'icon': 'bi bi-list-ol', 'label': 'Subir Carteiras'},
                     {'icon': 'bi bi-list-ol', 'label': "Carteira OP's"},
                     {'icon': 'bi bi-list-ol', 'label': 'Carteira Programação'},
                     {'icon': 'bi bi-folder-x', 'label': 'Alterar - Excluir OP'},
                     {'icon': 'bi bi-bootstrap-reboot', 'label': 'Alterar Plano Nest'},
                     {'icon': 'bi bi-person-lines-fill', 'label': 'Follow Up'},
                     {'icon': 'bi bi-bootstrap-reboot', 'label': 'Solicitar Reposição'},
                     {'icon': 'bi bi-bootstrap-reboot', 'label': "Previsão de Compras"}]},
    
        {'icon': 'bi bi-gear-wide-connected', 'label': 'Programação',
         'submenu': [{'icon': 'bi bi-list-ol', 'label': 'Lista de Programados'},
                     {'icon': 'bi bi-bootstrap-reboot', 'label': "OP's á Programar"},
                     {'icon': 'bi bi-cloud-download', 'label': "Baixar Nesting"}]},
    
        {'icon': 'bi bi-cart3', 'label': 'Compras',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Lista Geral'},
                     {'icon': 'bi bi-ui-checks', 'label': 'Conferência Almoxarifado'},
                     {'icon': 'bi bi-check2-circle', 'label': 'Finalizar Conferência'},
                     {'icon': 'bi bi-bag-check', 'label': 'Confirmar Recebimento'},
                     {'icon': 'bi bi-ui-checks', 'label': 'Agrupar para Cotação'},
                     {'icon': 'bi bi-cash-coin', 'label': 'Movimentação de Cotação'},
                     {'icon': 'bi bi-cart-plus', 'label': 'Solicitar Compra'},
                     {'icon': 'bi bi-cash-coin', 'label': 'Itens Comprados'},
                     {'icon': 'bi bi-box-arrow-in-down', 'label': 'Cadastrar Item'},
                     {'icon': 'bi bi-building', 'label': 'Cadastrar Fornecedor'},
                     {'icon': 'bi bi-cart-plus', 'label': 'Solicitar Orçamento'}]},
    
        {'icon': 'bi bi-file-diff', 'label': 'Qualidade',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Lista de PPM'},
                     {'icon': 'bi bi-folder-plus', 'label': 'Abrir SCI'},
                     {'icon': 'bi bi-arrow-repeat', 'label': 'Atualizar - Finalizar SCI'},
                     {'icon': 'bi bi-list-task', 'label': 'Lista de Instrumentos'},
                     {'icon': 'bi bi-file-earmark-ruled', 'label': 'Relatórios Qualidade'}]},
    
        {'icon': 'bi bi-send-plus', 'label': 'Serviço Externo',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Lista de Romaneio'},
                     {'icon': 'bi bi-folder-plus', 'label': 'Abrir Trabalho Externo'},
                     {'icon': 'bi bi-arrow-repeat', 'label': 'Atualizar Romaneio'},
                     {'icon': 'bi bi-check2-circle', 'label': 'Finalizar Romaneio'}]},
    
        {'icon': 'bi bi-truck', 'label': 'Expedição',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Lista de Romaneio'},
                     {'icon': 'bi bi-folder-plus', 'label': 'Abrir Romaneio'},
                     {'icon': 'bi bi-arrow-repeat', 'label': 'Atualizar Romaneio'},
                     {'icon': 'bi bi-check2-circle', 'label': 'Finalizar Romaneio'}]},
    
        {'icon': 'bi bi-person-raised-hand', 'label': 'RH',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Lista de Colaboradores'},
                     {'icon': 'bi bi-calendar2-week', 'label': 'Cartão Ponto'},
                     {'icon': 'bi bi-person-plus', 'label': 'Cadastrar Colaborador'},
                     {'icon': 'bi bi-person-plus', 'label': 'Cadastrar Usuario'}]},
    
        {'icon': 'bi bi-bar-chart', 'label': 'Indicadores'},
    
        {'icon': 'bi bi-person-circle', 'label': 'Conta',
         'submenu': [{'icon': 'bi bi-list-task', 'label': 'Ponto'},
                     {'icon': 'bi bi-person-plus', 'label': 'Configuração da Conta'}]},
    
        {'icon': 'bi bi-person-circle', 'label': 'Teste'}]

    
    tema = {'txc_inactive': 'black', 'menu_background': '#eaeaea', 'txc_active': 'black', 'option_active': '#ffffff', 'gap': '0rem'}
    opcao = hc.nav_bar(menu_definition=menu_opcao, home_name='Ambiente', override_theme=tema, sticky_mode='sticky', sticky_nav=False)

    if opcao == 'Teste':
        testes.teste()
