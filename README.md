# Portfolio de Ciberseguridad

Portfolio técnico orientado a seguridad defensiva, automatización con Python, revisión de configuración, análisis inicial de registros, seguridad web y laboratorios reproducibles.

## Qué puede revisar un headhunter
- Herramientas Python pequeñas y auditables en `tools/`.
- Procedimientos de hardening y respuesta a incidentes en `playbooks/`.
- Laboratorios de IA controlada, Docker y Wi-Fi CSI en `labs/`.
- Investigación de vulnerabilidades y modelado de amenazas en `research/`.
- Pruebas unitarias en `tests/`.
- Plantillas de informes y evidencias en `templates/`.
- Guía de publicación profesional en `docs/GITHUB_PUBLICACION.md`.

## Inicio rápido

Requiere Python 3.10+ y no necesita dependencias externas para las herramientas principales.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m unittest discover -s tests -v
python tools/tcp_inventory.py 127.0.0.1 --ports 22,80,443,8000
python tools/log_triage.py samples/auth.log --format json
python tools/config_audit.py samples/config-example.env
python tools/http_security_headers.py https://example.com
```

En Windows, activa el entorno con `.venv\Scripts\activate`.

## Proyectos

| Proyecto | Competencias | Ruta |
|---|---|---|
| Inventario TCP acotado | Python, sockets, tiempos de espera, JSON | `tools/tcp_inventory.py` |
| Revisión de cabeceras HTTP | Seguridad web, evaluación de controles | `tools/http_security_headers.py` |
| Triage de registros | Regex, agregación y detección heurística | `tools/log_triage.py` |
| Auditoría de configuración | Reglas explicables y redacción de valores | `tools/config_audit.py` |
| Diseño de ciberagente controlado | IA responsable, límites de herramientas, supervisión | `labs/ciberagente/README.md` |
| Wi-Fi CSI | Diseño experimental, telemetría y privacidad | `labs/wifi-csi/README.md` |
| Respuesta a incidentes y hardening | Procedimientos, evidencias y remediación | `playbooks/` |

## Uso responsable
Utiliza las herramientas únicamente contra sistemas propios o con autorización expresa. No incluyen explotación automática ni acciones destructivas. Los resultados son indicios y requieren revisión humana.

## Antes de publicar
Este paquete es una base de portfolio, no una afirmación de que las herramientas se hayan probado en producción. Ejecuta las pruebas, añade resultados reales y capturas propias saneadas, personaliza tu perfil y no publiques secretos, direcciones privadas sensibles ni datos personales.
