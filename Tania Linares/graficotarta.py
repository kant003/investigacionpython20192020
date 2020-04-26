from matplotlib import pyplot

paises =['Francia','España','EEUU','China','Italia','México','Reino Unido','Turquía','Alemania','Tailandia']

turistas = [86.9,81.8,75.9,60.7,58.2,39.3,37.7,37.6,37.5,35.4]

colores = ('blue','#2FAED5','yellow','#807E80','pink','brown','purple','red','green','orange')

valores= (0,0.2,0,0,0,0.4,0,0,0,0)

pyplot.rcParams['toolbar']='None'

_, _, texto = pyplot.pie(turistas,colors=colores,shadow=True, labels=paises, autopct='%1.1f%%',
explode=valores, startangle=180)

for tex in texto:
    tex.set_color('white')

#pyplot.axis('equal')

#pyplot.title('Grafica lenguajes programacion')

pyplot.legend(labels=paises)

pyplot.savefig('lenguajes.png')
pyplot.show()

