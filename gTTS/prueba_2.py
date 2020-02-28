from gtts import gTTS

tts = gTTS('Guardar el texto convertido a audio en un archivo con el metodo write_to_fp', lang='es-es')

with open("prueba_2.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)