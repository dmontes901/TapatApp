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
| :---        |  :---        |  :---        |  :---         |  :---     |  :--- | 
| Servei que consulta un User per Username  | http://192.168.144.158:10050/tapatapp/getUser |GET | application/json |  username (string) |
  
  - Resposta:
    
    Code 200 Ok: {id=1,"username":"dani", "password":"montes", "email":"danimontes@gmail.com"}

    Code 400 No trobat: {"error": "No trobat"}
