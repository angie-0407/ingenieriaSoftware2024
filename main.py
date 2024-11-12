from flask import Flask, jsonify, request

app = Flask(__name__)

# Endpoint Raiz
@app.route("/")
def root():
    return "Hola mundo, me llamo Angie"

@app.route("/users/<user_id>")
def get_user(user_id):
    user = {
        "id": user_id,
        "name": "Angie",
        "telefono": "88991122"
    }
    query = request.args.get("query")
    if query:
        user["query"] = query
    return jsonify(user), 200


#Endpoit para crear un usuario
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    data["status"] = "user created"
    return jsonify(data), 201

#Endpoint para actualizar un usuario
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    update_user = {
        "id": user_id,
        "name": data.get("name", "Angie"),
        "telefono": data.get("telefono", "88991122"),
        "status": "user updated"
    }
    return jsonify(update_user), 200

#Endpoint para borrar un usuario
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    response = {
        "id": user_id,
        "status": "user deleted"
    }
    return jsonify(response), 200

if __name__ == "__main__":
    app.run(debug=True)

