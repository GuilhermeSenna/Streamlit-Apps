import streamlit as st
from pytube import YouTube
import locale
import SessionState

session_state = SessionState.get(url='', yt=None)


def show_progress_bar(stream, chunk, file_handler, bytes_remaining):
    return  # do work

def main():
    st.title("Youtube Thumbnail Downloader")

    st.text('Enter a Youtube Video Complete URL')

    url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ&ab_channel=Jacob%2BKatieSchwarzJacob%2BKatieSchwarz'

    if not session_state.url or session_state == url:
        session_state.url = url

        # if st.button('Buscar o link'):
        session_state.yt = YouTube(url)

    st.header('Informações sobre o vídeo')

    st.markdown('---')

    id = session_state.url[session_state.url.find('=') + 1:session_state.url.find('&')]

    st.image('https://img.youtube.com/vi/'+id+'/maxresdefault.jpg')

    # Title of video
    st.markdown(f'**Title:** {session_state.yt.title}')

    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    # Number of views of video
    st.markdown(f'**Number of views:** {session_state.yt.views:n}')

    # Length of the video
    st.markdown(f'**Length of video:** {session_state.yt.length} seconds')

    # Rating
    st.markdown(f'**Ratings:** {session_state.yt.rating:.2f} of 5')

    # Description of video
    with st.beta_expander('Descrição do vídeo'):
        st.text(f'Description: \n\n{session_state.yt.description}')

    videos = session_state.yt.streams.filter(progressive=True).order_by('resolution').desc()

    # st.write(videos[0].res)

    radio = st.radio('Selecione a qualidade desejada: ', videos)

    if st.button('Download'):
        st.write(radio.download())
        st.progress(radio.register_on_progress_callback(show_progress_bar))

# yt.register_on_progress_callback(show_progress_bar)


if __name__ == '__main__':
    main()