# Dashboard de Seguridad Informática

Este proyecto consiste en un dashboard interactivo desarrollado en Python que proporciona información relevante sobre la seguridad informática de un sistema. El dashboard permite al usuario visualizar información relacionada con la seguridad, como la presencia de software desactualizado, contraseñas débiles, posibles ataques de phishing y la presencia de protección antivirus y antimalware.

## Funcionalidades

El dashboard incluye las siguientes funcionalidades:

1. **Software Desactualizado y Falta de Parches de Seguridad**: Verifica la versión del sistema operativo y del software instalado en un dispositivo y compara esta información con bases de datos de vulnerabilidades conocidas. Utiliza las bibliotecas `platform` y `requests` para obtener la información necesaria.

2. **Contraseñas Débiles o Predeterminadas**: Evalúa la fortaleza de las contraseñas almacenadas en un sistema y verifica si cumplen con ciertos criterios de seguridad (longitud, uso de caracteres especiales, etc.). Utiliza la biblioteca `passlib` para evaluar la complejidad de las contraseñas.

3. **Phishing y Ingeniería Social**: Ayuda en la detección de posibles ataques de phishing analizando los correos electrónicos en busca de patrones comunes utilizados en correos de phishing, como enlaces maliciosos o solicitudes de información sensible. Utiliza bibliotecas como `re` para análisis de texto.

4. **Falta de Protección Antivirus y Antimalware**: Verifica si un dispositivo tiene instalada y actualizada una solución de antivirus o antimalware. Puede hacerse mediante el acceso al registro del sistema o mediante la verificación de procesos en ejecución. Podría requerir bibliotecas específicas dependiendo del sistema operativo.

## Estructura del Proyecto

El proyecto sigue la siguiente estructura de archivos y carpetas:

dashboard_app/
│
├── data/
│ ├── passwords.txt
│ └── software_versions.json
│
├── resources/
│ ├── icono.png
│ └── estilos.css
│
├── scripts/
│ ├── seguridad.py
│ └── phishing.py
│
├── ui/
│ ├── main_window.ui
│ └── recursos.qrc
│
└── main.py


## Requisitos de Instalación

Para ejecutar este proyecto, se requiere tener instalado Python 3 y las siguientes bibliotecas:

- `pyqt5`: Para la interfaz gráfica.
- `passlib`: Para evaluar la complejidad de las contraseñas.
- `requests`: Para realizar solicitudes HTTP.
- Otras bibliotecas específicas según las funcionalidades requeridas (por ejemplo, `psutil` para verificar procesos en ejecución).

Puedes instalar las dependencias ejecutando el siguiente comando:

## Uso

Para ejecutar el dashboard, simplemente ejecuta el archivo main.py utilizando Python:

El dashboard se abrirá y podrás interactuar con él para visualizar la información de seguridad.

```bash
pip install pyqt5 passlib requests psutil

python main.py



