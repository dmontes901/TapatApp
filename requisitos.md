# Requeriments Tècnics

## 1. Backend (Servidor i Gestió de Dades)

El backend serà el cor del sistema, encarregat de gestionar dades, usuaris, i la lògica del sistema.

### a. Requisits del servidor
- **Allotjament**: AWS EC2, DigitalOcean o Heroku.
- **Base de dades**: MySQL, PostgreSQL o MongoDB.
- **Sistema operatiu del servidor**: Ubuntu 22.04, CentOS o Windows Server.
- **APIs i serveis web**: RESTful APIs amb JSON, GraphQL per consultes avançades.

### b. Llenguatges de programació
- Python (Flask), JavaScript (Apache NetBeans).

### c. Seguretat
- **Autenticació i autorització**: OAuth 2.0, JWT (JSON Web Tokens).
- **Xifratge de dades**: AES-256 per dades sensibles, TLS per comunicacions segures.
- **Còpies de seguretat automàtiques**: Configurades amb cron jobs i emmagatzemades en S3 o Google Cloud Storage.

---

## 2. Frontend

### a. Tipus de Clients
- Aplicacions Web (React, Angular, Vue.js), Aplicacions Mòbils (Flutter, React Native), Aplicacions Escriptori (Electron).

### b. Llenguatge de programació
- HTML5, CSS3, JavaScript (ES6+), TypeScript per projectes més grans.

### c. Compatibilitat dispositius
- Compatibilitat amb navegadors principals (Chrome, Firefox, Safari, Edge) i dispositius mòbils (iOS i Android).

---

## 3. Requisits Generals

### a. Gestió d'usuari i autenticació
- **Rols d’usuari**: Administrador, Editor, Usuari Final.
- **Base de dades**: MySQL amb taules específiques per a permisos i rols.
- **Seguretat**: MFA (Autenticació Multifactor), bloqueig d'IP després d'intents fallits.

### b. Emmagatzematge local i sincronització
- **Dades que es guarden en local**: Preferències de l'usuari i dades temporals.
- **Seguretat**: Xifratge AES per dades locals, sincronització segura amb TLS.

### c. Gestió d’accessibilitat
- Nivells **A**, **AA** i **AAA** segons les WCAG 2.1.

---

## 4. Requisits d'Infraestructura
- **Xarxa**: Connexió estable amb mínim 100 Mbps per al servidor.
- **Espai d’emmagatzematge al núvol**: S3 per a arxius estàtics, amb mínim 50 GB inicial.
- **APIs de tercers**: Stripe per a pagaments, SendGrid per a correus electrònics.

---

## 5. Requisits del Procés de Desenvolupament
- **IDE’s**: Visual Studio Code, IntelliJ IDEA, o PyCharm segons el llenguatge.
- **Control de Versions**: Git amb repositoris a GitHub, GitLab o Bitbucket.
- **Mètode de desenvolupament**: Scrum amb sprints de 2 setmanes i demos periòdiques.
- **Proves de qualitat (QA)**: Tests unitaris (JUnit, Jest), proves d'integració i proves d'usuari final amb Selenium.
