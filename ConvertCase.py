import streamlit as st
import SessionState
session_state = SessionState.get(text='')


def myfunc(word):
    return "".join(w.upper() if i % 2 else w.lower() for i, w in enumerate(word))


def main():
    st.title('Converter texto case')

    texto = st.text_area('Digite o texto aqui a ser convertido', session_state.text)

    col_A_1, col_A_2, col_A_3, col_A_4, col_A_5, col_A_6 = st.beta_columns(6)

    if col_A_1.button('lower case'):
        session_state.text = texto.lower()
    if col_A_2.button('UPPER CASE'):
        session_state.text = texto.upper()
    if col_A_3.button('Sentence case'):
        session_state.text = '. '.join(i.capitalize() for i in texto.split('. '))
    if col_A_4.button('Capitalize Case'):
        session_state.text = texto.title()
    if col_A_5.button('aLtErNaTiNg cAsE'):
        session_state.text = myfunc(texto)
    if col_A_6.button('InVeRsE CaSe'):
        session_state.text = ''.join(c.lower() if c.isupper() else c.upper() for c in texto)


    st.markdown('---')

    col_B_1, col_B_2, col_B_3 = st.beta_columns(3)

    if col_B_1.button('Download text'):
        pass
    if col_B_2.button('Copy to clipboard'):
        pass
    if col_B_3.button('Clear'):
        # 1 - Alterar o session_state.text não funciona
        # 2 - Dar ID a cada um dos widgets e depois incrementar causa bugs
        # como ter que apertar mais de uma vez em botão para ter a funcionalidade
        pass


if __name__ == '__main__':
    main()
