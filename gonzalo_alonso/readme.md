# Investigación de uso de Python y OpenCV para detectar y localizar objetos


## Detección de colores basado en el tutorial de [Adrian Rosebrock](https://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/)

Para usar los script de python se necesitan las siguientes librerías

`
deque, numpy, opencv-python
`

Se debe ejecutar el script __ball_detector__ indicando el fichero de video a usar con el modificador __-v__ o se usará  la webcam por defecto

El rango de color a detectar está configurado en el script como __ballLowerColor__ y  __ballUpperColor__. Este rango se obtiene de el script range_detector.py. Se pasará una captura de pantalla o foto en PNG como parámetro a este script para que se abran 3 ventanas, una con la imagen original, otra como la máscara resultado y la tercera es una coleccion de sliders que permite ajustar esta máscara. Al obtener la máscara adecuada tendremos los valores en esta ventana de sliders.


## Detección de caras basado en el tutorial de [Adarsh Menon](https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81)

En este script se pasará un fichero de video con el parámetro __-v__ o se usará la webcam por defecto