# Mi Proyecto

Bienvenido a mi proyecto. A continuación, encontrarás enlaces a los documentos clave para comprender su propósito y requisitos:

- [Descripción del Proyecto](descripcion.md)
- [Requisitos Técnicos](requisitos.md)

# HTTP

- [HTTP REQUEST](HTTPRequest.md)
- [HTTP RESPONSE](HTTPResponse.md)

# Definició dels EndPoints del Servei Web:
  - HOST: 192.168.144.158:10050

| Descripció  | End-point     | Method     |Tipus de petició|Parametres|
| :---        |  :---        |  :---        |  :---         |  :---     |
| Servei que consulta un User per Username  | http://192.168.144.158:10050/tapatapp/getUser |GET | application/json |  username (string) |
  
  - Còdigos de Resposta HTTP:
    
1. Code 200 Ok: {
  "status": "success",
  "data": {
    "username": "usuari1",
    "firstName": "Nom",
    "lastName": "Cognom",
    "email": "usuari1@example.com",
    "phone": "123456789",
    "address": "Carrer Exemple, 123"
  }
}

2. Code 400 No trobat: {"error": "No trobat"}
