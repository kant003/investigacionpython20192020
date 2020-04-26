#Importo los modulos necesarios
from matplotlib import pyplot
import numpy 

#Genero los datos para el gráfico
x = numpy.arange(-2.5,10,0.1)
y = x*numpy.cos(x)

#la segunda grafica la pinto a 90º
y1 = x*numpy.sin(90)


#Creo y Muestro el gráfico
pyplot.plot(x,y)

#nueva grafica
pyplot.plot(x,y1,':',linewidth=1,color='g',marker='x')

pyplot.title('Grafico Lineal')

#Grosor de línea
# Para modificar el grosor de línea basta con
#  incluir como argumento adicional en plot
#  la propiedad linewidth.
pyplot.plot(x,y,linewidth=4)

#Color de línea (en este caso rosa).
pyplot.plot(x,y,color='#eb34d8')

#Añadir regilla
pyplot.grid()

pyplot.show()