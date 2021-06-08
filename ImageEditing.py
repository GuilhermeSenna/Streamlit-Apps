import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# image = Image.open('sunrise.jpg')

st.title('Edição de imagem')

img = Image.new('RGB', (0, 0))

uploaded_file = st.file_uploader("Choose a image")
if uploaded_file is not None:
    try:
        img = Image.open(uploaded_file)

        # img = Image.new('RGB', (1000, 800), color=(73, 109, 137))
        draw = ImageDraw.Draw(img)

        imgWidth, imgHeight = img.size

        # print(width)

        text = st.text_input("Texto a inserir na imagem")

        colA, colB = st.beta_columns(2)
        centralizar_x = colA.checkbox('Centralizar no eixo x?')
        centralizar_y = colB.checkbox('Centralizar no eixo y?')

        col1, col2 = st.beta_columns(2)
        tamanho_fonte = col2.slider('Selecione o tamanho da fonte', 6, 160, 32)
        font = ImageFont.truetype("arial.ttf", tamanho_fonte)
        shadowColor = 'black'
        textColor = 'white'

        txtWidth, txtHeight = draw.textsize(text, font=font)

        # st.markdown('---')

        eixo_x = eixo_y = 0
        if centralizar_x:
            eixo_x = (imgWidth - txtWidth) // 2
        x_slider = col2.slider('Eixo X', 0, imgWidth - txtWidth, eixo_x)

        # st.markdown('---')

        if centralizar_y:
            eixo_y = (imgHeight - txtHeight) // 2

        y_slider = col2.slider('Eixo Y', 0, imgHeight - txtHeight, eixo_y)

        x = imgWidth - txtWidth - (imgWidth - txtWidth - x_slider)
        y = imgHeight - txtHeight - y_slider

        for adj in range(3):
            # move right
            draw.text((x - adj, y), text, font=font, fill=shadowColor)
            # move left
            draw.text((x + adj, y), text, font=font, fill=shadowColor)
            # move up
            draw.text((x, y + adj), text, font=font, fill=shadowColor)
            # move down
            draw.text((x, y - adj), text, font=font, fill=shadowColor)
            # diagnal left up
            draw.text((x - adj, y + adj), text, font=font, fill=shadowColor)
            # diagnal right up
            draw.text((x + adj, y + adj), text, font=font, fill=shadowColor)
            # diagnal left down
            draw.text((x - adj, y - adj), text, font=font, fill=shadowColor)
            # diagnal right down
            draw.text((x + adj, y - adj), text, font=font, fill=shadowColor)

        d = ImageDraw.Draw(img)
        # d.text((imgWidth/2, imgHeight-80), "Hello World", fill=(255, 255, 0))

        # create normal text on image
        draw.text((x, y), text, font=font, fill=textColor)

        # img.save('pil_text.png')

        col1.image(img, caption='Teste de imagem')
    except:
        st.error('O arquivo não é uma imagem ou está corrompido')
