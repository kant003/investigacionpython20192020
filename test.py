import pyweather


# OpenWeatherMap 

location = 'Salt Lake City, Utah, United States'
conditions = pyweather.openweather_conditions(location)
current_temp = conditions['main']['temp']
current_humidity = conditions['main']['humidity']
current_pressure = conditions['main']['pressure']


# Yahoo Weather 

location = 'New York City, New York, United States'
conditions = pyweather.yahoo_conditions(location)
current_condition = conditions['current_condition']
current_temp = conditions['current_temp']
current_date = conditions['date']
weather_code = conditions['code']
