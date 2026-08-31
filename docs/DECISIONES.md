# Registro de decisiones

## 2026-08-31 — Problema y dataset

- Se selecciona clasificación de cancelación de clientes de telecomunicaciones.
- Se adopta el dataset de Kaggle `blastchar/telco-customer-churn`.
- Motivo: combina variables numéricas y categóricas, tiene desbalance moderado y
  permite estudiar de forma visible el efecto del preprocesamiento sobre KNN.
- Tradeoff: es manejable para una entrega académica, pero no debe tratarse como
  una muestra representativa o causal del mercado actual.

## 2026-08-31 — Diseño experimental

- Un único split estratificado 80/20 con `random_state=42`.
- Un único estimador: KNN con `n_neighbors=7`.
- F1 de la clase positiva como métrica principal por el desbalance de `Churn`.
- Comparación entre preparación mínima y preparación limpia.
- Toda transformación aprendida se ajusta exclusivamente con `X_train`.

## 2026-08-31 — Colaboración

- Flujo GitHub Flow: rama corta por issue y PR hacia `main`.
- Commits con Conventional Commits.
- Integración del notebook a cargo de una sola persona para reducir conflictos.
- Merge por squash cuando los criterios de aceptación y la revisión estén
  completos.

## 2026-08-31 — Nuevo reparto de responsabilidades

- Se cambia el reparto acordado en la planeación inicial: el EDA completo (manual
  y automático) queda en una sola persona y el preprocesamiento completo en otra.
- Motivo: repartir esos dos frentes por herramienta dejaba a `srodrigub1` con dos
  bloques grandes y desequilibraba la carga.
- Reparto vigente: `srodrigub1` issues #2, #3 y #4; `Pacha-e` issues #5 y #6 más la
  integración; `Ang3l1485` issue #7.
- Consecuencia en el repositorio: `notebooks/work/02_eda_preprocesamiento.ipynb`
  pasa a llamarse `notebooks/work/02_preprocesamiento.ipynb` y cambia de dueño; el
  EDA automático se integra al notebook 01.
- El contrato experimental no cambia: mismo split, misma semilla y mismo estimador.

## 2026-08-31 — Preprocesamiento: umbrales declarados por el equipo

- Limpieza previa al split limitada a correcciones deterministas: formato de texto,
  tipo real de `TotalCharges`, duplicados exactos, exclusión de `customerID` y
  codificación del objetivo. Toda estadística aprendida ocurre después del split.
- `TotalCharges` se convierte a numérico y sus valores vacíos se declaran `NaN`; la
  imputación por mediana se ajusta solo con entrenamiento.
- Variante mínima: imputación necesaria más `OrdinalEncoder`, sin escalar. Se acepta
  a propósito el orden artificial en variables nominales.
- Variante limpia: `No internet service` y `No phone service` se colapsan a `No`
  dentro del pipeline por ser semánticamente redundantes.
- Umbral de correlación declarado por el equipo: `|r| >= 0.95` sobre entrenamiento.
- Umbral de VIF declarado por el equipo: `VIF >= 10`, con eliminación por rondas y
  cálculo manual mediante `LinearRegression`.
- Escalador elegido por evidencia: `RobustScaler` si alguna numérica supera 5 % de
  atípicos por 1,5·IQR; en caso contrario `MinMaxScaler`, para dejar las numéricas
  en el mismo rango [0,1] de las variables ficticias que compara KNN.

## 2026-08-31 — Entorno y compatibilidad del curso

- Se usa Python 3.12 y `uv.lock` como fuente reproducible de dependencias.
- Se conserva `ydata-profiling==4.18.4` porque el material de la materia importa
  `ydata_profiling.ProfileReport`, aunque la librería avisa que esa interfaz está
  deprecada.
- Se añade `setuptools<81` explícitamente porque esa versión de ydata-profiling
  usa `pkg_resources` sin declararlo como dependencia.
- El smoke test de importación terminó correctamente después de generar por
  primera vez la caché de fuentes de Matplotlib.
