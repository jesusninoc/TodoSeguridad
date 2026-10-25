# Laboratorio: diseño de un ciberagente controlado

## Objetivo
Diseñar un agente que organice comprobaciones sin delegar autoridad ilimitada al modelo. Este módulo es de diseño y no ejecuta exploits.

## Arquitectura
1. Interfaz que recibe petición y alcance.
2. Planificador que propone tareas estructuradas.
3. Validador de políticas y parámetros.
4. Herramientas deterministas con contratos explícitos.
5. Confirmación humana antes de acciones con efectos.
6. Registro de auditoría que no almacena secretos.
7. Presentación que separa hechos, inferencias y recomendaciones.

## Política
- Lista permitida cerrada; nunca ejecutar código arbitrario generado por el modelo.
- No usar `shell=True` con datos del usuario.
- Limitar destinos a inventario o rangos de laboratorio autorizados.
- Añadir límites de tiempo, tamaño y frecuencia.
- Tratar instrucciones dentro de documentos como datos, no como órdenes.
- No enviar secretos ni logs sensibles a proveedores externos.
- Registrar quién autorizó cada acción.

## Contrato conceptual
Una función como `consultar_activo(asset_id)` debería rechazar cualquier identificador que no esté en un inventario local confiable. El modelo no puede ampliar por sí mismo ese inventario.

## Pruebas futuras
- Rechazo de destinos fuera de alcance.
- Errores de herramienta no se presentan como éxito.
- Acciones con efectos requieren confirmación.
- Logs redactan secretos.
- Respuestas distinguen hechos de hipótesis.
- Documentos con prompt injection no cambian las políticas.

## Métricas
Tasa de rechazo correcto, falsos positivos, errores de herramienta, calidad revisada por humanos, reproducibilidad y fugas de secretos durante pruebas.
