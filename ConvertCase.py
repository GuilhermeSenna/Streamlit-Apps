import streamlit as st
import SessionState

# O input armazena a string que está no text_area
# O output armazena a conversão com o input
# Essa armazenagem é necessária pelo text_area vir antes do button
session_state = SessionState.get(input='', output='', key=0)


def myfunc(word):
    return "".join(w.upper() if i % 2 else w.lower() for i, w in enumerate(word))


def main():
    st.title('Converter texto case')

    # O text Area aparecerá aqui
    # Essa instanciação serve para demarcar aonde ele ficará
    area = st.empty()

    col_A_1, col_A_2, col_A_3, col_A_4, col_A_5, col_A_6 = st.beta_columns(6)


    if col_A_1.button('lower case'):
        session_state.output = session_state.input.lower()
    if col_A_2.button('UPPER CASE'):
        session_state.output = session_state.input.upper()
    if col_A_3.button('Sentence case'):
        session_state.output = '. '.join(i.capitalize() for i in session_state.input.split('. '))
    if col_A_4.button('Capitalize Case'):
        session_state.output = session_state.input.title()
    if col_A_5.button('aLtErNaTiNg cAsE'):
        session_state.output = myfunc(session_state.input)
    if col_A_6.button('InVeRsE CaSe'):
        session_state.output = ''.join(c.lower() if c.isupper() else c.upper() for c in session_state.input)

    st.markdown('---')

    col_B_1, col_B_2, col_B_3 = st.beta_columns(3)

    if col_B_1.button('Download text'):
        pass
    if col_B_2.button('Copy to clipboard'):
        pass
    if col_B_3.button('Clear'):
        # Limpando o Output é modificado o conteúdo do textarea
        session_state.output = ''

    # O text area é declarado aqui mas aparece acima dos botões
    # Isso serve para quando se clica em um dos botões poder alterar o conteúdo do text area em tempo de execução
    session_state.input = area.text_area('Digite o texto aqui a ser convertido', session_state.output,
                                         key=session_state.key)


#
if __name__ == '__main__':
    main()

# main()
