import requests

BASE_URL = 'http://127.0.0.1:5000/productos'

def imprimir_respuesta(descripcion, respuesta):
    print(f"\n--- {descripcion} ---")
    print(f"Código de estado HTTP: {respuesta.status_code}")
    print("Respuesta:", respuesta.json())

# 1. Consultar todo el catálogo
respuesta_todos = requests.get(BASE_URL)
imprimir_respuesta("Catálogo completo", respuesta_todos)

# 2. Consultar un producto que existe (Ej. 202)
respuesta_202 = requests.get(f'{BASE_URL}/202')
imprimir_respuesta("Consulta producto 202", respuesta_202)

# 3. Consultar un producto que NO existe (para probar el error 404)
respuesta_404 = requests.get(f'{BASE_URL}/999')
imprimir_respuesta("Consulta producto inexistente (999)", respuesta_404)

# 4. Registrar un nuevo producto
nuevo_item = {
    "producto": "Silla Gamer Ergonómica",
    "precio": 120.50,
    "stock": 5
}
respuesta_post = requests.post(BASE_URL, json=nuevo_item)
imprimir_respuesta("Registrar nuevo producto", respuesta_post)