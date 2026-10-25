# Laboratorio Docker aislado

- Crea una red Docker dedicada para el laboratorio.
- Evita publicar puertos en todas las interfaces si no es necesario.
- No montes el directorio personal completo dentro de contenedores.
- No introduzcas claves SSH ni credenciales de producción.
- Fija versiones de imágenes cuando necesites reproducibilidad.
- Elimina contenedores y volúmenes con datos de prueba al terminar.

```bash
docker network create lab-security
docker network inspect lab-security
```

Utiliza imágenes de procedencia confiable. Mantén las aplicaciones vulnerables en un entorno aislado y sin rutas hacia redes de producción. Publica configuración saneada y resultados reproducibles.
