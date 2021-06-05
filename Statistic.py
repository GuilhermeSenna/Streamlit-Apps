import random
import numpy as np
import streamlit as st
from scipy import stats
import SessionState

session_state = SessionState.get(array=[])



def main():
    st.title('Cálculos estatísticos simples')

    # tamanho = st.slider('Definir tamanho do array', 5, 100000)

    # not session_state.array gera erro
    if st.button('Randomizar números') or session_state.array == []:
        session_state.array = np.random.randint(1, 99, 10)
        session_state.array.sort()

    radio = st.radio('Forma de visualização', ['Linha', 'Coluna'])

    if radio == 'Linha':
        st.text(session_state.array)
    else:
        st.write(session_state.array)

    st.markdown('---')

    st.text(f'Média: {np.mean(session_state.array)}')

    st.text(f'Mediana: {np.median(session_state.array)}')

    st.text(f'Moda: {stats.mode(session_state.array)[0][0]}, {stats.mode(session_state.array)[1][0]}x')

    st.text(f'Desvio padrão (σ): {np.std(session_state.array)}')

    st.text(f'Variância (σ²): {np.var(session_state.array)}')

    quartil = st.slider('Percentil (%)', 0, 100)

    st.text(np.percentile(session_state.array, quartil))


if __name__ == '__main__':
    main()
