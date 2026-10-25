# Playbook: hardening Linux y SSH

> Aplica cambios primero en una VM o con acceso a consola de recuperación. Un error puede bloquear el acceso remoto.

## Revisión SSH
Evalúa, según la distribución y el modelo de acceso, opciones como:

```text
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
MaxAuthTries 4
X11Forwarding no
```

No desactives contraseñas hasta probar la autenticación por clave en una segunda sesión. Comprueba los ficheros incluidos por la configuración de tu distribución.

## Procedimiento
1. Guarda copia de configuración.
2. Ejecuta `sshd -t` si está disponible.
3. Mantén abierta una sesión de recuperación.
4. Recarga el servicio siguiendo el procedimiento del sistema.
5. Abre una segunda sesión y comprueba el acceso.
6. Revisa logs y documenta el resultado.

## Sistema
- Instala actualizaciones con un proceso de cambios.
- Desactiva servicios innecesarios.
- Limita puertos con firewall y segmentación.
- Usa cuentas individuales y privilegio mínimo.
- Prueba restauraciones de copias.
- Centraliza registros y sincroniza la hora.

Publica únicamente diffs saneados; nunca claves, credenciales o logs sensibles.
