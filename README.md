# Mi Proyecto

Bienvenido a mi proyecto. A continuación, encontrarás enlaces a los documentos clave para comprender su propósito y requisitos:

- [Descripción del Proyecto](descripcion.md)
- [Requisitos Técnicos](requisitos.md)

# HTTP

- [HTTP REQUEST](HTTPRequest.md)
- [HTTP RESPONSE](HTTPResponse.md)

# Definición de los EndPoints del Servicio Web:
  - HOST: 192.168.144.158:5000

| Descripción  | End-point     | Method     |Tipus de petició|Parametres|
| :---        |  :---        |  :---        |  :---         |  :---     |
| Servicio que consulta un User por Username  | http://192.168.144.158:5000//tapatapp/getUser |GET | application/json |  username |
  
  - Còdigos de Resposta HTTP:
    
### 1. Code 200 Ok:
{
"status": "success",
  "data": {
    "username": "usuari1",
    "firstName": "Nom",
    "lastName": "Cognom",
    "email": "usuari1@example.com",
    "phone": "123456789",
    "address": "Carrer Mor, 123"
    }
}

### 2. 400 Bad Request - La sol·licitud està mal formada o li falten paràmetres:
{
"status": "error",
  "message": "Paràmetre 'username' no proporcionat o incorrecte"
}
### 3. 401 Unauthorized - No s'ha autenticat correctament:
{
  "status": "error",
  "message": "No autoritzat. Necessites autenticar-te per accedir a aquesta informació."
}
### 4. 403 Forbidden - L'usuari no té permís per consultar la informació:
{
  "status": "error",
  "message": "Accés prohibit. No tens permís per veure aquesta informació."
}

### 5. 404 Not Found - L'usuari no es troba a la base de dades:
{
  "status": "error",
  "message": "Usuari no trobat"
}
### 6. 422 Unprocessable Entity - La sol·licitud està ben formada, però el servidor no pot processar la informació proporcionada (per exemple, si el nom d'usuari té un format invàlid):
{
  "status": "error",
  "message": "Format de 'username' invàlid. 
  Si us plau, revisa el teu input."
}

### 7. 500 Internal Server Error - S'ha produït un error intern al servidor:
{
  "status": "error",
  "message": "Error intern al servidor. Si us plau, torni-ho a provar més tard."
}
# URL para probar las posibles salidas:
http://192.168.144.158:5000//tapatapp/getUser?name=usuari1

## Datos de entrada del usuario

### Inicio

- Contacta con nosotros: Consultar al equipo de soporte técnico especificando las dudas, que contiene un formulario en el que debe poner su correo y el problema.
- Registro: El usuario debe registrarse con un correo electrónico válido y una contraseña que incluya letras y números.
- Login: Se hará mediante email y contraseña.
  - He olvidado mi contraseña: El usuario si no recuerda su contraseña, podrá recuperarla poniendo el correo con el que se registró. Se le enviará un enlace para cambiar la contraseña.

### Pantalla principal

- Niños a cargo: Listado de niños bajo el cuidado del usuario.
  - Horas activas del pegat: Muestra la información del pegat sobre el niño/a a cargo (horas puesto, horas a retirar/colocar).
- Configuración: El usuario puede modificar la configuración dentro de la app.
  - Editar perfil: Modificar sus datos personales, añadir información o el apartado personal.
  - Configuraciones generales: Personalizar el aspecto de la aplicación (diseño de interfaz, modo oscuro, tamaño de texto).
- Cerrar sesión: Confirmar el cierre de sesión.

## Interfaz TapatApp
- [Interfaz](InterfazTapatApp.mmd)
