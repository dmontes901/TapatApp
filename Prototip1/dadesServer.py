# dadesServer.py
from flask import Flask, jsonify

# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def to_dict(self):
        """Devuelve el usuario como un diccionario sin la contraseña."""
        return {"id": self.id, "username": self.username, "email": self.email}

# Lista de usuarios (simulando una base de datos)
users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

# Clase Child
class Child:
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time

    def to_dict(self):
        return {
            "id": self.id,
            "child_name": self.child_name,
            "sleep_average": self.sleep_average,
            "treatment_id": self.treatment_id,
            "time": self.time
        }

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6)
]

# Clase Role
class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def to_dict(self):
        return {"id": self.id, "type_rol": self.type_rol}

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

# Clase Status
class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

# Clase Treatment
class Treatment:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "name": self.name}

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='Percentage')
]

# Crear aplicación Flask
app = Flask(__name__)

# Ruta para obtener todos los usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([user.to_dict() for user in users])

# Ruta para obtener un usuario por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u.id == user_id), None)
    if user:
        return jsonify(user.to_dict()), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

# Ruta para obtener todos los niños
@app.route('/children', methods=['GET'])
def get_children():
    return jsonify([child.to_dict() for child in children])

# Ruta para obtener un niño por ID
@app.route('/children/<int:child_id>', methods=['GET'])
def get_child(child_id):
    child = next((c for c in children if c.id == child_id), None)
    if child:
        return jsonify(child.to_dict()), 200
    return jsonify({"error": "Niño no encontrado"}), 404

# Ruta para obtener todos los roles
@app.route('/roles', methods=['GET'])
def get_roles():
    return jsonify([role.to_dict() for role in roles])

# Ruta para obtener todos los estados
@app.route('/statuses', methods=['GET'])
def get_statuses():
    return jsonify([status.to_dict() for status in statuses])

# Ruta para obtener todos los tratamientos
@app.route('/treatments', methods=['GET'])
def get_treatments():
    return jsonify([treatment.to_dict() for treatment in treatments])

# Ejecutar el servidor
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
