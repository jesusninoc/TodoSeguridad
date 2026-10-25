# Catálogo de proyectos

## 1. Inventario TCP acotado
**Ruta:** `tools/tcp_inventory.py`  
Comprueba conectividad TCP de una lista explícita de puertos. No identifica versiones ni vulnerabilidades. Un timeout no demuestra que el puerto esté cerrado.

## 2. Revisión de cabeceras HTTP
**Ruta:** `tools/http_security_headers.py`  
Obtiene cabeceras y señala controles comunes ausentes. La ausencia de una cabecera no confirma por sí sola una vulnerabilidad.

## 3. Triage de registros
**Ruta:** `tools/log_triage.py`  
Cuenta patrones de autenticación fallida y marca fuentes que superan un umbral. Es una heurística, no sustituye a un SIEM ni demuestra compromiso.

## 4. Auditoría de configuración
**Ruta:** `tools/config_audit.py`  
Busca patrones de riesgo en ficheros de texto y evita mostrar valores que podrían contener secretos.

## 5. Ciberagente controlado
**Ruta:** `labs/ciberagente/README.md`  
Diseño de agente con lista permitida de herramientas, alcance explícito, confirmación humana y registros de auditoría.

## 6. Wi-Fi CSI
**Ruta:** `labs/wifi-csi/README.md`  
Plan experimental para recoger telemetría en laboratorio y explicar factores de confusión, privacidad y límites de inferencia.

## 7. Playbooks defensivos
**Ruta:** `playbooks/`  
Respuesta a incidentes, hardening Linux/SSH, revisión web y priorización de vulnerabilidades.

## Para convertir un proyecto en caso de estudio
Incluye objetivo, alcance, arquitectura, requisitos, pasos reproducibles, resultado real saneado, pruebas, limitaciones, falsos positivos y mitigación verificada.
