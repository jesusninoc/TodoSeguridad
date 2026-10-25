# Playbook: revisión defensiva web

## Alcance
Registra dominio, rutas, cuentas de prueba, ventana de evaluación y límites de frecuencia. No pruebes funciones que modifiquen datos reales sin autorización.

## Lista de comprobación
- [ ] HTTPS y configuración TLS mantenida.
- [ ] Cookies de sesión con Secure, HttpOnly y SameSite cuando proceda.
- [ ] CSP adaptada a los recursos legítimos.
- [ ] Protección CSRF en operaciones con estado cuando corresponda.
- [ ] Autorización en servidor para cada recurso.
- [ ] Validación de entradas y codificación de salidas.
- [ ] Errores sin stack traces ni secretos.
- [ ] Dependencias inventariadas y actualizadas.
- [ ] Secretos fuera del repositorio.
- [ ] Logs con minimización de datos.
- [ ] CORS limitado a orígenes necesarios.
- [ ] Endpoints administrativos protegidos.

## Plantilla de hallazgo
Título / activo / fecha / evidencia saneada / impacto / severidad razonada / mitigación / prueba posterior / falsos positivos.
