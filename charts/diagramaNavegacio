flowchart TD;
    %% Inicio
    A["Pantalla de Inicio"] -->|Iniciar Sesión| B["Pantalla de Login"];
    A -->|Registrarse| C["Pantalla de Registro"];
    A -->|Recuperar Contraseña| D["Pantalla de Recuperación"];

    %% Inicio de Sesión
    B -->|Credenciales Correctas| E["Dashboard"];
    B -->|Credenciales Incorrectas| B1["Error: Credenciales Incorrectas"] --> B;
    B -->|Olvidé mi contraseña| D;

    %% Registro
    C -->|Datos Válidos| C1["Verificación de Email"];
    C1 -->|Código Correcto| E;
    C1 -->|Código Incorrecto| C2["Error: Código Inválido"] --> C1;
    C -->|Datos Inválidos| C3["Error: Datos Incorrectos"] --> C;

    %% Recuperación de Contraseña
    D -->|Ingresar Email| D1["Enviar Código"];
    D1 -->|Código Enviado| D2["Ingresar Código"];
    D2 -->|Código Correcto| D3["Crear Nueva Contraseña"];
    D3 -->|Contraseña Guardada| B;
    D2 -->|Código Incorrecto| D4["Error: Código Inválido"] --> D2;

    %% Navegación en la App
    E -->|Perfil| F["Pantalla de Perfil"];
    E -->|Configuración| G["Pantalla de Configuración"];
    E -->|Cerrar Sesión| A;

    %% Retornos
    F --> E;
    G --> E;
