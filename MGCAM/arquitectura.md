```mermaid
flowchart LR
    subgraph Cliente
        A[🧑‍💻 Navegador Web]
        B[📄 HTML/CSS/JS - Interfaz de usuario]
    end

    subgraph Servidor [Servidor Backend]
        C[🌐 Flask (Python)]
        D[🔒 Lógica de autenticación]
        E[🖼️ Control de imágenes]
        F[🗄️ Conexión a MySQL]
    end

    subgraph Base_de_datos
        G[(MySQL)]
    end

    A --> B
    B --> C
    C --> D
    D -->|Consulta de usuario y contraseña| F
    C --> E
    E -->|Consultar imágenes según usuario| F
    F --> G
```
