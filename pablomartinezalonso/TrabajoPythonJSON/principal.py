import json
import requests


ruta = 'data.json'


def escribir_datos(ruta):
    data = {}
    data['encantamientos'] = []

    data['encantamientos'].append({
        'nombre': 'Protección',
            'resumen':'Reduce considerablemente el daño de todo tipo de ataque',
            'maximo_nivel':4,
            'items':['casco','peto','grebas','botas']
    })

    data['encantamientos'].append({
        'nombre': 'Protección contra el fuego',
            'resumen':'Reduce el daño causado por el fuego',
            'maximo_nivel':4,
            'items':['casco','peto','grebas','botas']
    })

    data['encantamientos'].append({
        'nombre': 'Caída de pluma',
            'resumen':'Reduce el daño causado por caídas',
            'maximo_nivel':4,
            'items':'botas'
    })

    data['encantamientos'].append({
        'nombre': 'Protección contra explosiones',
            'resumen':'Reduce el daño causado por explosiones',
            'maximo_nivel':4,
            'items':['casco','peto','grebas','botas']
    })

    data['encantamientos'].append({
        'nombre': 'Protección contra proyectiles',
            'resumen':'Reduce el daño contra los proyectiles',
            'maximo_nivel':4,
            'items':['casco','peto','grebas','botas']
    })

    data['encantamientos'].append({
        'nombre': 'Respiración',
            'resumen':'Aumenta la capacidad pulmonar bajo el agua',
            'maximo_nivel':3,
            'items':'casco'
    })

    data['encantamientos'].append({
        'nombre': 'Afinidad acuática',
            'resumen':'Aumenta la visión dentro del agua y mejora el rendimiento de las herramientas usadas',
            'maximo_nivel':1,
            'items':'casco'
    })

    data['encantamientos'].append({
        'nombre': 'Espinas',
            'resumen':'Los enemigos que te atacan reciben un 50 porciento del daño que te causaron',
            'maximo_nivel':3,
            'items':['casco','peto','grebas','botas']
    })

    data['encantamientos'].append({
        'nombre': 'Agilidad acuática',
            'resumen':'Permite nadar más rápido en el agua.',
            'maximo_nivel':3,
            'items':'botas'
    })

    with open(ruta, 'w') as contenido:
        json.dump(data, contenido, indent=5)


def leer_datos(ruta):
    with open(ruta) as contenido:
        data = json.load(contenido)
        for dato in data['encantamientos']:
            print('')
            print('Nombre del encantamiento:',dato['nombre'])
            print('Resumen:',dato['resumen'])
            print('Nivel maximo:',dato['maximo_nivel'])
            print('Items que puedes encantar:',dato['items'])
            print('')




def acceder_api():
    nombre_evolucion = input('Introduce el nombre del pokemon del que se quiere saber la evolución: ')
    url = 'https://pokeapi.co/api/v2/pokemon/' + nombre_evolucion
    resp = requests.get(url)
    r=json.loads(resp.content)
    species = r['species']['url']
    resp = requests.get(species)
    r=json.loads(resp.content)
    evo = r['evolution_chain']['url']
    resp = requests.get(evo)
    r=json.loads(resp.content)
    name = r['chain']['evolves_to'][0]['species']['name']
    print(name)

    with open('datos.json', 'w') as archivo:
        json.dump(r, archivo, indent=5)


opcion = 0
print('LEER Y ESCRIBIR ARCHIVOS JSON CON PYTHON')
while opcion!=4:
    
    print('Escribir archivos (1) || Leer archivos (2) || Acceder a una API (3) || Salir (4)')
    opcion = int(input('Opcion: '))

    if opcion==1:
        print('')
        print('ESCRITURA DE DATOS...')
        print('')
        escribir_datos(ruta)
    if opcion==2:
        print('')
        print('LECTURA DE DATOS...')
        print('-------------------------------------------------')
        leer_datos(ruta)
    if opcion==3:
        print('')
        print('ACCEDER A API')
        print('')
        acceder_api()





