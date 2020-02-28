from gtts import gTTS

tts = gTTS('Guardar el texto convertido a audio en un archivo con el metodo save', lang='es-es')
tts.save("prueba_1.mp3")