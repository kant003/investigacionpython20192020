from gtts import gTTS
from playsound import playsound

NOMBRE_ARCHIVO = "sonido_generado.mp3"
tts = gTTS('Hola mi amol estas viendo lol tu solo en serio', lang='ja')

with open(NOMBRE_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)

playsound(NOMBRE_ARCHIVO)