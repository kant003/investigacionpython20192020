from matplotlib import pyplot
import numpy 

from mpl_toolkits.mplot3d import Axes3D
 
fig = pyplot.figure()
ax = Axes3D(fig)
X = numpy.arange(-8, 30, 0.50)
Y = numpy.arange(-8, 20, 0.50)
X, Y = numpy.meshgrid(X, Y)
R = numpy.sqrt(X**2 + Y**2)
Z = numpy.sin(R)
 
ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
pyplot.show()