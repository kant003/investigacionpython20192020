
# imports
import requests, json 

# Api
api_key = "dbf84d386d59bb6487f1645392b51cb3"

# Url peticion 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Nombre de la ciudad
nombreCiudad = input("Introduce el nombre de la ciudad : ") 


# Url + ciudad + Key 
# http://api.openweathermap.org/data/2.5/weather?q=London&APPID=dbf84d386d59bb6487f1645392b51cb3
complete_url = base_url +  "q=" + nombreCiudad + "&APPID=" + api_key 
print(complete_url)

# Mandamos la peticion por get
# guardamos el objeto
response = requests.get(complete_url) 

# Pintamos el Json con todos los datos que devuelve  
print(response.json() )
x = response.json() 


# Si no devuelve 404 
if x["cod"] != "404": 


	y = x["main"] 


	# Temperatura
	temp = y["temp"] 


	# Presion atmosferica
	press = y["pressure"] 

	# Humedad

	humedad = y["humidity"] 

	z = x["weather"] 

	# Descripcion del cielo ( nublado , despejado ...)
	
	descripcion = z[0]["description"] 

	# print following values 
	print(" Temperatura (in kelvin unit) = " +
					str(temp) +
		"\n Presion atmosferica  = " +
					str(press) +
		"\n Humedad (en porcentaje) = " +
					str(humedad) +
		"\n Descripcion  = " +
					str(descripcion)) 

else: 
	print(" No se ha encontrado la ciudad  ") 
