# Notebooks de trabajo

Estos notebooks separan el trabajo paralelo y reducen conflictos del formato
JSON de Jupyter. No son los artefactos finales de entrega.

- `01_datos_eda_manual.ipynb`: `srodrigub1`, issues #2, #3 y #4.
- `02_preprocesamiento.ipynb`: `Pacha-e`, issues #5 y #6.
- `03_modelado_comparacion.ipynb`: `Ang3l1485`, issue #7.

## Límites de cada notebook

| Notebook | Trabajo que le corresponde | Trabajo que no debe adelantar |
|---|---|---|
| `01_datos_eda_manual.ipynb` | Fuente, calidad, diccionario, auditoría, EDA manual sobre entrenamiento, EDA automático con `ydata-profiling` y contraste entre ambos | No construir los pipelines definitivos ni entrenar o evaluar KNN |
| `02_preprocesamiento.ipynb` | Congelar el split común, construir las variantes mínima y limpia, analizar atípicos/correlación/VIF solo para decidir transformaciones y exportar matrices | No desarrollar el EDA general, calcular métricas del modelo, comparar desempeños ni redactar conclusiones del experimento |
| `03_modelado_comparacion.ipynb` | Cargar las matrices entregadas por el notebook 02, entrenar el mismo KNN(7), calcular métricas y comparar ambas variantes | No volver a dividir el dataset, recalcular imputaciones/escaladores ni cambiar las columnas preparadas |

La breve prueba de KNN del notebook 02 solo comprueba que sus matrices aceptan el
estimador acordado. No calcula métricas, no usa `y_test` para evaluar y no sustituye
el modelado del notebook 03.

## Archivos de entrada y traspaso

### Notebook 01: datos y EDA

- CSV principal: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`.
- Referencia obligatoria del split: `artifacts/preprocesamiento/split_referencia.csv`.
- Debe conservar las variables originales para hacer el EDA y seleccionar como
  entrenamiento únicamente los identificadores marcados como `train`.
- No debe partir de las matrices codificadas o escaladas del notebook 02.

### Notebook 02: preprocesamiento

- CSV principal: `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`.
- Produce el split común y los siguientes archivos para el notebook 03:
  `X_train_minimo.csv.gz`, `X_test_minimo.csv.gz`, `X_train_limpio.csv.gz`,
  `X_test_limpio.csv.gz`, `y_train.csv.gz` y `y_test.csv.gz`.
- También produce `contrato_preprocesamiento.json`, `split_referencia.csv` y
  `tabla_transformaciones.csv` como evidencia y trazabilidad.

### Notebook 03: modelado y comparación

- Carpeta de entrada: `artifacts/preprocesamiento/`.
- Debe cargar los seis archivos `.csv.gz` generados por el notebook 02 mediante
  `pd.read_csv(ruta, index_col=0)`. Pandas detecta automáticamente la compresión.
- No debe comenzar desde el CSV crudo: hacerlo repetiría el preprocesamiento y
  podría cambiar el split o las columnas, invalidando la comparación.
- Antes de entrenar debe comprobar que los índices de cada `X` coincidan con su
  archivo `y` y leer `contrato_preprocesamiento.json` para confirmar KNN(7), semilla,
  tamaños y métrica primaria.

La carpeta `artifacts/` no se versiona. Para obtener estas entradas se debe ejecutar
el notebook 02 completo después de descargar y verificar el CSV crudo, o recibir los
artefactos del responsable de preprocesamiento por el canal acordado por el equipo.

Reparto acordado el 31 de agosto de 2026: una persona concentra todo el EDA
(manual y automático) y otra todo el preprocesamiento, en lugar de repartir esos
dos frentes por herramienta. El registro está en `docs/DECISIONES.md`.

El integrador mueve al notebook maestro únicamente bloques ejecutados, revisados
y respaldados por el PR correspondiente.
