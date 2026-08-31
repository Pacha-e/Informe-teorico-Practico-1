# Contrato del problema

## Pregunta de negocio

Con la información disponible al cierre de un periodo, ¿qué clientes tienen
mayor riesgo de cancelar el servicio en el periodo siguiente, para priorizar
acciones de retención?

## Formulación de aprendizaje automático

- Tipo de tarea: clasificación binaria supervisada.
- Unidad de análisis: un cliente.
- Variable objetivo: `Churn`.
- Clase positiva: `Yes`.
- Momento de predicción: cierre del periodo, antes de conocer la cancelación.
- Variables predictoras: todas las columnas salvo `Churn` y `customerID`.
- Exclusión: `customerID` es un identificador, no una característica.
- Modelo común de la comparación: `KNeighborsClassifier(n_neighbors=7)`.
- Partición común: 80 % entrenamiento y 20 % prueba, estratificada, con
  `random_state=42`.
- Métrica principal: F1 de `Churn=Yes`.
- Métricas secundarias: accuracy, precision, recall y matriz de confusión.

## Dos variantes exigidas

1. **Pipeline mínimo ejecutable:** únicamente las conversiones y codificaciones
   indispensables para que KNN pueda entrenar.
2. **Pipeline limpio:** tratamiento de tipos, faltantes, codificación,
   redundancia y escalado, aprendido exclusivamente con datos de entrenamiento.

El split debe hacerse antes de aprender imputaciones, escaladores, categorías o
cualquier otra estadística de preparación. Ambas variantes deben usar
exactamente la misma partición y el mismo clasificador para que la comparación
sea válida.

## Criterio de éxito académico

El trabajo está completo cuando el notebook explica y ejecuta sin errores el
ciclo problema → datos → EDA manual → EDA automático → preparación mínima →
preparación limpia → KNN → comparación → conclusiones; además, cada decisión
está respaldada por evidencia calculada sobre entrenamiento.

## Límites de interpretación

El conjunto es una muestra didáctica y sus clientes no representan
necesariamente una población real actual. El modelo estima asociación
predictiva, no demuestra que una acción de retención cause una reducción del
churn. No se deben presentar sus resultados como una política causal.

## Decisiones aún abiertas

- Confirmar con el docente la definición exacta solicitada de `IQRratio`.
- Registrar fecha, hora y canal de entrega.
- Confirmar si, además del `.ipynb` y el PDF, se admite algún anexo.
