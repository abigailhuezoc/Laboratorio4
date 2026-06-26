from flask import Flask, jsonify, request

app = Flask(__name__)

# Catálogo inicial en memoria
catalogo = [
    {"codigo": 201, "producto": "Teclado mecánico RGB", "precio": 45.00, "stock": 12},
    {"codigo": 202, "producto": "Mouse inalámbrico", "precio": 18.50, "stock": 25},
    {"codigo": 203, "producto": "Monitor LED 24\"", "precio": 165.00, "stock": 8}
]

# 1. Consulta del catálogo completo (GET)
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(catalogo), 200

# 2. Consulta de un producto específico (GET)
@app.route('/productos/<int:codigo>', methods=['GET'])
def obtener_producto(codigo):
    producto = next((prod for prod in catalogo if prod["codigo"] == codigo), None)
    if producto is not None:
        return jsonify(producto), 200
    return jsonify({"error": f"El producto con código {codigo} no existe."}), 404

# 3. Registro de nuevos productos (POST)
@app.route('/productos', methods=['POST'])
def agregar_producto():
    datos = request.get_json()
    if not datos or 'producto' not in datos or 'precio' not in datos or 'stock' not in datos:
        return jsonify({"error": "Faltan datos requeridos (producto, precio, stock)."}), 400
    
    nuevo_codigo = max(prod["codigo"] for prod in catalogo) + 1 if catalogo else 1
    nuevo_producto = {
        "codigo": nuevo_codigo,
        "producto": datos["producto"],
        "precio": float(datos["precio"]),
        "stock": int(datos["stock"])
    }
    catalogo.append(nuevo_producto)
    return jsonify(nuevo_producto), 201

if __name__ == '__main__':
    app.run(debug=True)