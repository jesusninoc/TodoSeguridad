# Laboratorio: Wi-Fi CSI y telemetría

## Objetivo
Explorar la recogida y el análisis de Channel State Information (CSI) en un entorno controlado, sin exagerar las conclusiones que pueden extraerse.

## Requisitos
Una placa compatible con la API CSI del fabricante, firmware apropiado, ordenador de desarrollo y ubicaciones de prueba marcadas. La compatibilidad depende de chipset, SDK, modo Wi-Fi y configuración.

## Diseño experimental
1. Registra placa, revisión, firmware, canal, ancho de banda y ubicación.
2. Mantén fijos los puntos de emisión y recepción.
3. Recoge una línea base sin cambios deliberados.
4. Repite mediciones con variaciones controladas.
5. Anota interferencias, pérdidas de paquetes y cambios ambientales.
6. Separa entrenamiento y evaluación si usas modelos.
7. Repite en diferentes condiciones.

## Factores de confusión
Multipath, mobiliario, movimiento fuera del área, interferencias, orientación de antenas, variación de hardware y cambios de canal.

## Privacidad
Las señales pueden permitir inferencias sobre actividad. Obtén consentimiento cuando corresponda, minimiza datos y evita vigilar personas sin base legítima. Publica datos sintéticos o agregados cuando sea posible.

## Interpretación
Una variación CSI no demuestra por sí sola que haya una persona. Hace falta protocolo experimental, métricas, tasa de falsos positivos, evaluación independiente y límites claros.

CSV sugerido: `timestamp_utc,device_id,channel,sequence,feature_1,feature_2,label`. Evita publicar SSID privados, MAC de terceros o datos identificativos.
