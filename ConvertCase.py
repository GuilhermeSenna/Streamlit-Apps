import SessionState
import base64
import streamlit as st
import pyperclip


# The input stores the string that is in text_area
# The output stores the conversion with the input
# This storage is needed because textarea comes before the button
session_state = SessionState.get(input='', output='', key=0)


# Function used to generate the download
def download_link(object_to_download, download_filename, download_link_text):
    # if isinstance(object_to_download, pd.DataFrame):
    #     object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


def myfunc(word):
    return "".join(w.upper() if i % 2 else w.lower() for i, w in enumerate(word))


def main():
    st.title('Text case converter')

    # The text Area will appear here
    # This instantiation serves to demarcate where it will be
    area = st.empty()

    col_A_1, col_A_2, col_A_3, col_A_4, col_A_5, col_A_6 = st.beta_columns(6)

    if col_A_1.button('lower case'):
        session_state.output = session_state.input.lower()
        st.success('Lower case applied')

    if col_A_2.button('UPPER CASE'):
        session_state.output = session_state.input.upper()
        st.success('Upper case applied')

    if col_A_3.button('Sentence case'):
        session_state.output = '. '.join(i.capitalize() for i in session_state.input.split('. '))
        st.success('Sentence case applied')

    if col_A_4.button('Capitalize Case'):
        session_state.output = session_state.input.title()
        st.success('Capitalize case applied')

    if col_A_5.button('aLtErNaTiNg cAsE'):
        session_state.output = myfunc(session_state.input)
        st.success('Alternating case applied')

    if col_A_6.button('InVeRsE CaSe'):
        session_state.output = ''.join(c.lower() if c.isupper() else c.upper() for c in session_state.input)
        st.success('Inverse case applied')

    st.markdown('---')

    col_B_1, col_B_2, col_B_3 = st.beta_columns(3)

    if col_B_1.button('Download text'):
        tmp_download_link = download_link(session_state.output, 'text.txt', 'Click here to download your text!')
        st.markdown(tmp_download_link, unsafe_allow_html=True)
    if col_B_2.button('Copy to clipboard'):
        pyperclip.copy(session_state.output)

        st.success('Text copied to clipboard')
    if col_B_3.button('Clear'):
        # If the user has not pressed any button, there is no output yet, so it is necessary to increment...
        # ...the text_area key to clear completely.
        session_state.key += 1

        # If it has been pressed, it is necessary to clear the Output to clear the text_area as well.
        session_state.output = ''
        st.success('Successfully cleared text area')


    # The text area is declared here but appears above the buttons
    # This is for when you click on one of the buttons to be able to change the content of the text area at run time
    session_state.input = area.text_area('Enter text here to be converted', session_state.output,
                                         key=session_state.key)


if __name__ == '__main__':
    main()