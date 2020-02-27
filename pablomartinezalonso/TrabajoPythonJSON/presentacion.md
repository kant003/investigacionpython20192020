# Leer y escribir archivos JSON con Python

La forma mas sencilla de generar un archivo JSON desde Python es exportando los datos en un diccionario. Estos pueden contener cualquier tipo de dato: valores numéricos, cadenas de texto, booleanos, etc.

Todo esto lo haremos mediante el uso del paquete json.

---

## El paquete json

Para empezar a utilizarlo en el inicio del archivo escribiremos:

> <pre>import json</pre>

### La funcion json.dump()

Transforma un diccionario de Python en una cadena de texto en formato JSON.

> <pre>with open('data.json', 'w') as file: <br/>    json.dump(data, filea)</pre>

Esta función tiene algunos modificadores como por ejemplo __ensure_ascii__ que modifica la codificación de texto empleada en el archivo.

> <pre>json.dump(data, file, ensure_ascii=False)</pre>

El modificador __indent__ que genera un sangrado en el archivo JSON.

> <pre>json.dump(data, file, indent=4)</pre>

O el modificador __sort_keys__ que se utiliza para ordenar por la clave

> <pre>json.dumps(data, sort_keys=True)</pre>

### La funcion json.load()

Transforma una cadena de texto que contiene un objeto JSON en un diccionario de Python

> <pre>with open('data.json') as file: <br/>    data = json.load(file)</pre>

---


