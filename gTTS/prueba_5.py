from gtts import gTTS
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us', slow=True)
tts.save("prueba_5.mp3")