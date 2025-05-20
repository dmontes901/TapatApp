# 📸 Gestor de Imágenes con Login de Usuarios
Este proyecto es una aplicación desarrollada en Python que permite la gestión dinámica de imágenes a través de una interfaz sencilla y personalizada según el usuario que inicia sesión.

## 🛠️ Características principales
- 🔐 Autenticación de usuarios: 
El sistema implementa un mecanismo de autenticación basado en credenciales, donde los usuarios deben ingresar su nombre de usuario y contraseña para acceder a las funcionalidades protegidas. La contraseña se almacena utilizando una función hash (MD5 en este caso), mejorando así la seguridad frente a accesos no autorizados.

- 👥 Soporte para múltiples roles de usuario (por ejemplo, user1, admin), con acceso diferenciado a contenidos.

- 🖼️ Visualización de imágenes según el usuario autenticado.

- 📂 Navegación intuitiva mediante una barra de navegación integrada.

- 🗄️ Base de datos MySQL para almacenar la información de usuarios y rutas de imágenes.

## 💡 Objetivo
Ofrecer una solución simple pero eficaz para mostrar imágenes personalizadas según el perfil del usuario, ideal como base para sistemas de gestión de contenido, portafolios privados o dashboards con contenido multimedia restringido.

## 💻 Funcionalidades



# ⚙️ Requisitos Técnicos
## 🎨 Frontend
### Wireframes/Interfaz:

- HTML5 + CSS3 básico (plantillas Jinja2 desde Flask)

- Estilo simple y responsive con CSS puro

### Arquitectura de carpetas:

- /templates → Archivos .html (renderizados por Flask)

- /static → Imágenes, CSS y otros recursos estáticos

### Ruta de imágenes:

- Las imágenes se cargan desde static/uploads/

- Se muestran dinámicamente en home.html según el usuario conectado

### Navegación/Flujo:

- Pantalla de login

- Vista principal (home.html) tras inicio de sesión

- Visualización de imágenes asociadas al usuario

## 🖥️ Backend
### Lenguaje:

- Python 3.x

### Framework:

- Flask (aplicacion ligera, manejo de rutas y gestión de sesiones)

### Base de datos:

- MySQL (almacenamiento estructurado de usuarios e imágenes)

- Conexión mediante mysql-connector-python o similar

### Control de versiones:

- Git + GitHub (versionar el código y colaborar)

### Testing:

- unittest para validar la lógica del backend y endpoints

### Seguridad:

- Contraseñas encriptadas (con MD5)

## Modelo E/R

![image](https://github.com/user-attachments/assets/08b09712-ac63-47d3-8a7c-5863d0c34d0d)

## Diagrama de arquitectura

![image](https://github.com/user-attachments/assets/5fbce81d-b65b-4aa4-a21b-0b4a8b30139d)

# 🔌 End-points WebService

| **Método** | **Endpoint**       | **Función**                                                   |
|------------|--------------------|----------------------------------------------------------------|
| `POST`     | `/login`           | Inicia sesión de usuario con nombre de usuario y contraseña (MD5). |
| `POST`     | `/register`        | Registra un nuevo usuario en la base de datos.                |
| `GET`      | `/imagenes`        | Lista imágenes visibles según el usuario autenticado.         |
| `POST`     | `/imagenes`        | Sube una nueva imagen (requiere permisos especiales, ej. admin). |
| `GET`      | `/perfil`          | Devuelve la información del perfil del usuario actual.        |
| `PUT`      | `/perfil`          | Permite modificar los datos del perfil del usuario.           |
| `POST`     | `/logout`          | Cierra la sesión del usuario actual.                          |

## Diagrama de clases BackEnd

![image](https://github.com/user-attachments/assets/0414979f-b52f-47a8-bf16-11d8c52ce316)


### Creado por Daniel Montes y Jose Gomez - 2025
