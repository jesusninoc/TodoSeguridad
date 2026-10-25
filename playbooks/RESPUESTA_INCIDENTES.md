# Playbook: respuesta a incidentes

## 1. Preparación
Mantén inventario de activos, responsables, contactos, copias de seguridad, sincronización horaria y procedimientos de escalado.

## 2. Identificación
Registra quién reporta, cuándo y qué se observó. Separa hechos de hipótesis. Clasifica impacto en confidencialidad, integridad y disponibilidad.

## 3. Contención
Sigue el procedimiento aprobado. Valora si hay que preservar memoria o estado volátil antes de apagar. Aísla de forma proporcional y documentada; no borres logs para limpiar el sistema.

## 4. Evidencias
Registra fecha con zona horaria, sistema, operador, herramienta y versión. Calcula hashes cuando proceda, conserva el original en almacenamiento restringido y trabaja sobre copias.

## 5. Erradicación y recuperación
Determina la causa raíz con evidencia suficiente, corrige el vector inicial, rota credenciales afectadas, aplica parches validados y prueba restauraciones.

## 6. Cierre
Resume cronología, impacto, decisiones y tareas pendientes. Comunica a las partes autorizadas y asigna responsables y fechas a las mejoras.

| Hora y zona | Hecho observado | Fuente | Confianza | Acción |
|---|---|---|---|---|
| AAAA-MM-DD HH:MM | Descripción verificable | Log / alerta | Alta/Media/Baja | Acción |
