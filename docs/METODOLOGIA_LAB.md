# Metodología de laboratorio

## Antes de empezar
Registra propietario, activos, direcciones autorizadas, ventana de pruebas, técnicas permitidas, criterios de parada y contacto responsable.

## Entorno
- Usa VM o contenedor propio y, cuando sea posible, red aislada.
- Crea un snapshot antes de cambiar configuraciones.
- Utiliza datos ficticios.
- Evita exponer servicios vulnerables a Internet.
- No montes el directorio personal completo en un contenedor.

## Ejecución
Registra fecha, versión de herramienta, parámetros y resultado. Repite la prueba para evaluar consistencia. Conserva evidencias originales en privado y publica solo copias saneadas.

## Hallazgos
Cada hallazgo debe indicar activo, condición observada, evidencia mínima, impacto potencial, incertidumbre, severidad razonada, mitigación y prueba posterior.

## Cierre
Revierte cambios temporales, comprueba que no quedan servicios expuestos y documenta las limitaciones.
