import streamlit as st
from streamlit_modal import Modal


def apontamento():
    colb1, colb2, colb3 = st.columns([2.4, 3, 1])
    with colb2:
        st.markdown('imagem')
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
       
            st.markdown('______________________________')


    st.title('')



