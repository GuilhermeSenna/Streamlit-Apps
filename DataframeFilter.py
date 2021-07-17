import streamlit as st
import SessionState
import pandas as pd

# Dicionário
pesso = {
    'Nome': ['Guilherme', 'Fulana', 'Ciclano', 'Deltrana'],
    'Idade': [22, 14, 50, 30],
    'Sexo': ['M', 'F', 'M', 'F'],
    'Salario': [2000, 5000, 10000, 7300]
}

# Conversão para Dataframe
df = pd.DataFrame(data=pesso)

# Armazenagem por sessão
session_state = SessionState.get(pessoas=df)


# Função main
def main():
    st.title('Dataframe Filter')

    st.header('Programa que filtra valores de um Dataframe Pandas')

    # Parametros para restrição
    parametros = st.selectbox(
        "Restringir: ",
        ('Nenhum', 'Idade', 'Sexo', 'Salario'))

    # conversão definitiva para Dataframe Pandas
    pessoas = pd.DataFrame(session_state.pessoas)

    # Restrição para parâmetros
    if parametros == 'Idade':
        radio_idade = st.radio('Escolha o intervalo', ['Maior que', 'Menor que', 'Intervalo'])

        if radio_idade == 'Maior que':
            input_idade = st.number_input('Digite o intervalo entre a idade', step=1)
            pessoas = pessoas[pessoas["Idade"] > input_idade]
        elif radio_idade == 'Menor que':
            input_idade = st.number_input('Digite o intervalo entre a idade', step=1, value=100)
            pessoas = pessoas[pessoas["Idade"] < input_idade]
        else:
            col1, col2 = st.beta_columns(2)
            menor = col1.number_input('Menor que', step=1)
            maior = col2.number_input('Maior que', step=1, value=100)
            pessoas = pessoas[(pessoas['Idade'] < maior) & (pessoas['Idade'] > menor)]

    elif parametros == 'Sexo':
        sexo_select = st.selectbox(
            "Escolha o sexo desejado: ",
            ('M', 'F'))

        if sexo_select == 'M':
            pessoas = pessoas[pessoas["Sexo"] == 'M']
        else:
            pessoas = pessoas[pessoas["Sexo"] == 'F']
    elif parametros == 'Salario':
        radio_salario = st.radio('Escolha o intervalo', ['Maior que', 'Menor que', 'Intervalo'])

        if radio_salario == 'Maior que':
            input_salario = st.number_input('Digite o intervalo entre o salário', step=1)
            pessoas = pessoas[pessoas["Salario"] > input_salario]
        elif radio_salario == 'Menor que':
            input_salario = st.number_input('Digite o intervalo entre o salário', step=1, value=100)
            pessoas = pessoas[pessoas["Salario"] < input_salario]
        else:
            col1, col2 = st.beta_columns(2)
            menor = col1.number_input('Menor que', step=1)
            maior = col2.number_input('Maior que', step=1, value=12000)
            pessoas = pessoas[(pessoas['Salario'] < maior) & (pessoas['Salario'] > menor)]

    # Mostrando a tabela
    st.table(pessoas)


if __name__ == '__main__':
    main()
