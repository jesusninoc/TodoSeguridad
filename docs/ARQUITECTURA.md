# Arquitectura del portfolio

## Principios
- Código pequeño, revisable y con un objetivo concreto.
- Alcance explícito y parámetros validados.
- Sin explotación automática ni ejecución de comandos arbitrarios.
- Datos sintéticos y pruebas reproducibles.
- Resultados con limitaciones y revisión humana.
- Privacidad por diseño: no incluir secretos ni datos personales reales.

## Flujo de trabajo
1. Definir alcance y autorización.
2. Preparar un laboratorio aislado.
3. Ejecutar una prueba de bajo impacto.
4. Guardar la salida original de forma privada.
5. Sanear evidencias antes de publicarlas.
6. Interpretar hallazgos y documentar incertidumbres.
7. Aplicar una mitigación y verificarla.
8. Registrar mejoras pendientes.

## Límites de confianza
Las entradas se consideran no confiables. Las herramientas no deben ejecutar órdenes suministradas por un modelo de IA. Los resultados automáticos no son certificados de seguridad.
