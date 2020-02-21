#Importo los modulos necesarios
from matplotlib import pyplot
import numpy 

#nombre
fig= pyplot.figure('Calificaciones')

#datos eje x
x=['Jorge','Alex','Pablo','Diego','Ruben']
x2=['Pablo','Tania','Ricardo','Gonzalo','Yago']

#datos eje y
y = numpy.array([7.8,5.9,8.0,10,6.6])
y2 = numpy.array([9.0,5.0,8.3,7.7,9.5])


pyplot.bar(x,y,align='center')

#pongo color y lo alineo al centro.
pyplot.bar(x2,y2,color='g',align='center')

pyplot.title('Grafica de Barras')

#nonmbre eje x
pyplot.xlabel('Alumnos')
#nonmbre eje y
pyplot.ylabel('Media Notas')

#leyenda
pyplot.legend(['Clase 1ºDam','Clase 2ºDam'])

pyplot.show()