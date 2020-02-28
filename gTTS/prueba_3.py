from gtts import gTTS
tts = gTTS('Hola mundo. Estamos convirtiendo texto a voz con Python.', lang='es-us')
tts_ingles = gTTS('Hello world! testing tts in Python', lang='en')
tts_frances = gTTS('Bonjour le monde! test de tts en Python', lang='fr-fr')

with open("prueba_3.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)
    tts_ingles.write_to_fp(archivo)
    tts_frances.write_to_fp(archivo)