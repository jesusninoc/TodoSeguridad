# Modelo de amenazas para una aplicación web

## Activos
Cuentas y sesiones, datos de usuario, secretos, disponibilidad, registros y despliegue.

## Límites de confianza
Navegador-aplicación, aplicación-base de datos, aplicación-proveedor externo, CI/CD-despliegue y operador-consola administrativa.

## STRIDE
- Suplantación: robo o reutilización de sesión.
- Manipulación: modificación no autorizada.
- Repudio: falta de trazabilidad.
- Divulgación: exposición de datos o secretos.
- Denegación de servicio: agotamiento de recursos.
- Elevación de privilegios: autorización insuficiente.

## Controles
Autenticación fuerte, mínimo privilegio, consultas parametrizadas, registros minimizados, límites de recursos, gestión de secretos, revisión de dependencias y pruebas de recuperación.

Entregable: diagrama de flujo de datos, amenazas, controles y pruebas verificables.
