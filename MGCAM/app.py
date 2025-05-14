from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import hashlib
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'root'

# Conexión a MySQL
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=%s AND password=%s", (usuario, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['usuario'] = usuario
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error='Credenciales incorrectas')
    return render_template('login.html')

@app.route('/home')
def home():
    if 'usuario' not in session:
        return redirect('/login')
    return render_template('home.html', usuario=session['usuario'])

@app.route('/api/imagenes')
def api_imagenes():
    if 'usuario' not in session:
        return jsonify({'error': 'No autenticado'}), 401

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Obtener el ID del usuario autenticado
    cursor.execute("SELECT id FROM usuarios WHERE username = %s", (session['usuario'],))
    user = cursor.fetchone()

    if not user:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Usuario no encontrado'}), 404

    # Obtener las imágenes asociadas al usuario
    cursor.execute("SELECT titulo, descripcion, ruta_imagen, fecha_subida FROM imagenes WHERE usuario_id = %s", (user['id'],))
    imagenes = cursor.fetchall()

    cursor.close()
    conn.close()

    # Formatear la fecha de subida
    for img in imagenes:
        img['fecha_subida'] = img['fecha_subida'].strftime('%Y-%m-%d')

    return jsonify(imagenes)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = hashlib.md5(request.form['password'].encode()).hexdigest()
        email = request.form['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, password, email) VALUES (%s, %s, %s)",
                       (usuario, password, email))
        conn.commit()
        conn.close()

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
