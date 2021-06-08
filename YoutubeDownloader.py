import streamlit as st
from pytube import YouTube
import locale
import SessionState
import time


session_state = SessionState.get(url='', yt=None, progress=0)


previousprogress = 0
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        session_state.progress = liveprogress


def main():
    st.title("Youtube Thumbnail Downloader")

    # st.text('')

    url = st.text_input('Enter a Youtube Video Complete URL')

    try:

        if not session_state.url or session_state.url != url:
            print('to aqui agora')
            session_state.url = url

            # if st.button('Buscar o link'):
            session_state.yt = YouTube(url)

        st.header('Informações sobre o vídeo')

        st.markdown('---')

        if '&' in session_state.url:
            id = session_state.url[session_state.url.find('=') + 1:session_state.url.find('&')]
        else:
            id = session_state.url[session_state.url.find('=') + 1:]

        st.image('https://img.youtube.com/vi/'+id+'/maxresdefault.jpg')

        # Title of video
        st.markdown(f'**Title:** {session_state.yt.title}')

        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        # Number of views of video
        st.markdown(f'**Number of views:** {session_state.yt.views:n}')

        # Length of the video
        if session_state.yt.length < 3600:
            st.markdown(f'**Length of video:** {time.strftime("%M:%S", time.gmtime(session_state.yt.length))} Min')
        else:
            st.markdown(f'**Length of video:** {time.strftime("%H:%M:%S", time.gmtime(session_state.yt.length))} Hour')

        # Rating
        st.markdown(f'**Ratings:** {session_state.yt.rating:.2f} of 5 ({int((session_state.yt.rating/5)*100)}% approval)')

        # Description of video
        with st.beta_expander('Descrição do vídeo'):
            st.text(f'Description: \n\n{session_state.yt.description}')

        videos = session_state.yt.streams.filter(progressive=True).order_by('resolution').desc()

        # st.write(videos[0].res)

        st.header('Opções de download')

        st.markdown('---')

        radio = st.radio('Selecione a qualidade desejada: ', videos)

        if round(radio.filesize/(1024*1024)) != 0:
            st.write(f'Tamanho do vídeo: {round(radio.filesize/(1024*1024))} MB')
        else:
            st.write(f'Tamanho do vídeo: {round(radio.filesize / (1024))} KB')

        if st.button('Download'):
            session_state.yt.register_on_progress_callback(on_progress)
            st.write(radio.download())

            st.progress(session_state.progress)

    except:
        pass


# yt.register_on_progress_callback(show_progress_bar)


if __name__ == '__main__':
    main()