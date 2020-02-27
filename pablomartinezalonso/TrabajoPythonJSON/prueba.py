import json

estudiante = {'nombre completo': ['Juan', 'Pérez', 'Sánchez'], 'rol': 'estudiante'}

estudiante_json = json.dumps(estudiante, ensure_ascii=False)

print(estudiante_json)