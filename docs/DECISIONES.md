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

## 2026-08-31 — Entorno y compatibilidad del curso

- Se usa Python 3.12 y `uv.lock` como fuente reproducible de dependencias.
- Se conserva `ydata-profiling==4.18.4` porque el material de la materia importa
  `ydata_profiling.ProfileReport`, aunque la librería avisa que esa interfaz está
  deprecada.
- Se añade `setuptools<81` explícitamente porque esa versión de ydata-profiling
  usa `pkg_resources` sin declararlo como dependencia.
- El smoke test de importación terminó correctamente después de generar por
  primera vez la caché de fuentes de Matplotlib.
