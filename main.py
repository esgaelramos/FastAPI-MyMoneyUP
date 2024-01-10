import uvicorn

from core.application import app



if __name__ == "__main__":
    """
        Inicia el servidor FastAPI utilizando Uvicorn.
        - Inicia el servidor en el host 127.0.0.1 y el puerto 8000.
        - Configurado para recargar automáticamente en caso de cambios en el código.
        - Utiliza 8 trabajadores para manejar las solicitudes de manera concurrente.
        (Los workers no funcionaran mientras el reload este en True)
    """
    uvicorn.run(
        app="main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True, 
        workers=8
    )