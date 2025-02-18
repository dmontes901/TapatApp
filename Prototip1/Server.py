from flask import Flask, request, jsonify

# Clase User que representa un usuario en memoria
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def to_dict(self):
        """ Devuelve un diccionario sin la contraseña. """
        return {"id": self.id, "username": self.username, "email": self.email}

# Lista de usuarios (simula una base de datos)
listUsers = [
    User(id=1, username="usuari1", password="12345", email="usuari1@gmail.com"),
    User(id=2, username="usuari2", password="123", email="usuari2@gmail.com"),
    User(id=3, username="usuari3", password="00", email="Miscos@gmail.com")
]

# DAO para gestionar usuarios
class DAOUsers:
    def __init__(self):
        self.users = listUsers

    def get_user_by_username(self, username):
        """ Devuelve el usuario si existe, None si no. """
        for u in self.users:
            if u.username == username:
                return u
        return None

# Instancia de DAO
daousers = DAOUsers()

# Crear aplicación Flask
app = Flask(__name__)

@app.route('/tapatapp/getUser', methods=['GET'])
def get_user():
    username = request.args.get('name')  # Obtener parámetro de la URL

    if not username:
        return jsonify({"error": "Falta el parámetro 'name'"}), 400

    user = daousers.get_user_by_username(username)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/prototip/getuser/<string:username>', methods=['GET'])
def prototip_get_user(username):
    user = daousers.get_user_by_username(username)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

# Ejecutar el servidor en modo debug
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
