# Comandos para Migración con Alembic y SQLAlchemy

## 1. Inicializar un Proyecto Alembic:
<div class="termy">
```console
$ alembic init -t async migrations
```
</div>

## 2. Configuración del Archivo alembic.ini:
Asegúrate de configurar correctamente el archivo alembic.ini con la URL de tu base de datos.


## 3. Generar una Migración:
<div class="termy">
```console
$ alembic revision --autogenerate -m "Descripción de la migración"
```
</div>


## 4. Aplicar Migraciones:
<div class="termy">
```console
$ alembic upgrade head
```
</div>

## 5. Aplicar una Migración Específica:
<div class="termy">
```console
$ alembic upgrade <identificador>
```
</div>

**Estos comandos te ayudarán a trabajar con Alembic y SQLAlchemy para gestionar migraciones de bases de datos en tu proyecto. Asegúrate de ajustar los comandos según la configuración específica de tu aplicación y la versión de Alembic que estés utilizando.**

<details markdown="1">
<summary>Tener en cuenta: </summary>
Ten en cuenta que los modelos nuevos que se vayan agregando deben estar importados en el directorio `core/databases/models/__init__.py` como en el siguiente ejemplo:
```Python
from . import Endpoints
from . import EndpointsGroups
from . import EndpointsRoles
...
# Demás importaciones
```
</details>