# Talk Organizer API
Proyecto para la organizacion, control y administracion del servidor "Python Colombia" desde un sitio de administacion que este conectada
mediante un bot de discord, al servidor de Python Colombia.

## Ejecutar la Aplicación Localmente

1. **Instalación de Dependencias**: Asegúrate de tener Python y pip instalados. Luego, crear un entorno virtual y activarla para luego instalar las dependencias del proyecto.
    ```bash
    python3 -m venv <nombre del entorno>    # Para Linux
    python -m venv <nombre del entorno>     # Para Windows

    pip install -r requirements.txt --no-cache-dir
    ```

2. **Ejecutar la Aplicación sin utilizar docker**:
    ```bash
    python3 main.py     # Para Linux
    python main.py      # Para Windows
    ```

    La aplicación estará disponible en `http://localhost:8000`.

## Ejecutar la Aplicación con Docker Compose

1. **Construir la Imagen de Docker**:
    ```bash
    docker-compose build
    ```

2. **Ejecutar la Aplicación con Docker Compose**:
    ```bash
    docker-compose up
    ```

    La aplicación estará disponible en `http://localhost:8000`.

## Configuracion del pre-commit
1. **Ejecutar el pre-commit**:
    ```bash
    pre-commit autoupdate
    pre-commit install
    ```
    - El pre-commit funciona para las validaciones del flake8 y black formatter antes de realizar el commit, en caso de no cumplir con los
    estándares pep8 y docstrings, en caso de no cumplirlas mostrará los errores en consola antes de aplicar el commit

## Contribuciones

¡Contribuciones son bienvenidas! Por favor, sigue las pautas en [CONTRIBUTING.md].

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE] para obtener más detalles.

[CONTRIBUTING.md]: CONTRIBUTING.md
[LICENSE]: LICENSE
