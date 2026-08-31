# Plan técnico maestro — Informe Teórico Práctico 1

> Documento de trabajo generado con apoyo de IA. **No copiar su prosa al notebook entregable.**
> El PDF de la materia permite IA para código, pero exige que descripciones,
> justificaciones, explicaciones, análisis y conclusiones sean redactadas con
> palabras propias por los estudiantes; incumplirlo reduce la nota en 60%.

## 1. Fuentes de verdad y estado inicial

Fuente autoritativa de la entrega:
[`informeTeoricoPrac1.pdf`](./informeTeoricoPrac1.pdf), 8 páginas.

El 30 de agosto de 2026 también se auditó el material completo disponible en la
carpeta padre `Fundamentos de aprendizaje automático`. La ruta de aprendizaje que
declara `Table of Contents.html` es: repaso de Pandas → adquisición/limpieza →
`limpiezaDatos.ipynb` → `EDA.ipynb` → `aplicarModeloML(2).ipynb`.

| Fuente local | Qué fija para esta entrega |
|---|---|
| `presentacionDelCurso (1).pdf` | Informe 1 = 15%, grupos de máximo 3, semana 5, entrega por Interactiva, no se reciben entregas tarde. |
| `Fundamentos (1).pdf` | Aprendizaje supervisado y ciclo CRISP-DM; el problema y el impacto de negocio deben guiar el modelo. |
| `lecturaCasosCicloVida (1).pdf` | Accuracy alta no garantiza impacto; incorporar contexto de dominio y distinguir evaluación técnica de negocio. |
| `ambienteDesarrollo (1).pdf` | Python en Colab o local; NumPy, Pandas, Matplotlib, Seaborn y scikit-learn como base. |
| `AdquisicionLimpiezaDatos.pdf` | Limpieza, fuga, encoding, correlación, VIF, scaling y transformación logarítmica. |
| `limpiezaDatos.ipynb` | Implementaciones de Pandas/scikit-learn y `category_encoders.BinaryEncoder`. |
| `EDA.ipynb` | EDA manual y EDA automático con `ydata_profiling.ProfileReport`. |
| `aplicarModeloML(2).ipynb` | Split 80/20; KNN, SVC y Random Forest para clasificación; Random Forest, R² y MAE para regresión. |
| `repasoPython (2).pdf`, `repasoPandas.pdf` y HTML asociados | Sintaxis de soporte; no agregan una obligación estadística distinta. |
| `BonoPython/` | Entrega anterior y material ampliado de Python; sirve como referencia operativa, no como parte del Informe 1. |

Las copias de los PDF/notebooks presentes dentro de `BonoPython/` tienen el mismo
SHA-256 que las copias de la carpeta padre; no son versiones académicas diferentes.
El enunciado de la carpeta del informe también coincide byte a byte con el de la
carpeta padre.

Estado del proyecto:

- El dataset canónico ya está descargado localmente y verificado, pero permanece
  ignorado por Git. SHA-256:
  `88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a`.
- Ya existen el repositorio local, la estructura reproducible, el entorno
  bloqueado y el esqueleto del notebook. Aún no existen el análisis final, el
  modelo, las métricas, los gráficos definitivos ni el PDF de entrega.
- El canal está resuelto: **Interactiva**. Falta confirmar la fecha/hora exacta y
  la convención de nombre visibles en la plataforma.
- No se encontró una rúbrica cuantitativa separada del enunciado.
- Entorno local verificado con Python 3.12.13 y 140 paquetes resueltos en
  `uv.lock`; incluye Pandas, scikit-learn, JupyterLab, ydata-profiling y las
  demás dependencias del curso.

## 2. Definición de “hecho”

La entrega está terminada solo cuando existen y se abren correctamente:

1. `Informe_Teorico_Practico_1.ipynb`, ejecutado de principio a fin sin errores.
2. `Informe_Teorico_Practico_1.pdf`, exportado desde esa misma ejecución y con
   código, tablas, figuras y textos completos.

Además debe cumplirse todo lo siguiente:

- Problema de negocio, procedencia del dataset, tipo de tarea y target definidos.
- Split realizado antes de cualquier transformación que aprenda de los datos.
- EDA manual sobre entrenamiento, incluido el `IQRratio` una vez que el profesor
  confirme qué fórmula quiso indicar.
- EDA automático con `ydata-profiling`, exactamente la herramienta vista en clase.
- Codificación completamente numérica, Pearson/Spearman, VIF manual y escalamiento.
- Dos variantes comparables: dataset mínimamente limpio y dataset limpio.
- Mismo split, estimador, hiperparámetros y métricas en ambas variantes.
- Resultados interpretados honestamente, incluso si el dataset limpio no mejora.
- Todo texto evaluado redactado y revisado por los tres estudiantes.
- Fuente y licencia del dataset citadas.

## 3. Contrato explícito del enunciado

| Página | Obligación |
|---|---|
| 2 | Grupo de máximo 3; entregar `.ipynb` y PDF del notebook. |
| 3 | IA solo como apoyo de código; narrativa autoral; penalización del 60%. |
| 4 | Problema/contexto, justificación y origen del dataset, clasificación o regresión, target exacto. |
| 5 | Portales sugeridos para localizar datasets. |
| 6 | Partir antes de limpiar; limpiar por particiones; codificar; analizar correlación/multicolinealidad; escalar; justificar. |
| 7 | EDA manual, tendencia central/dispersión/posición, `IQRratio`, visualizaciones y comparación con EDA automático. |
| 8 | Mismo modelo sobre datos mínimamente limpios y limpios; comparar desempeño; conclusiones comparativas y generales. |

## 4. Decisiones que deben cerrarse antes de implementar

### Un bloqueo conceptual real: `IQRratio`

La auditoría completa encontró lo siguiente:

- `EDA.ipynb` enseña `IQR = Q3 - Q1` y los límites de outliers
  `Q1 - 1.5*IQR` y `Q3 + 1.5*IQR`.
- `AdquisicionLimpiezaDatos.pdf` solo vuelve a mencionar los cuartiles al explicar
  `RobustScaler`.
- El término literal `IQRratio` aparece únicamente en el enunciado; ningún material
  de clase proporciona fórmula, umbral ni interpretación.
- La bibliografía externa tampoco permite adivinarlo de forma segura: se encuentran
  convenciones como `Q3/Q1`, `IQR/mediana` y el coeficiente cuartílico
  `(Q3-Q1)/(Q3+Q1)`.

Por tanto, enviar al docente esta pregunta textual antes de programar esa celda:

> En el Informe 1, ¿`IQRratio` corresponde a `Q3/Q1`, a `IQR/mediana`, al
> coeficiente `(Q3-Q1)/(Q3+Q1)` u otra fórmula? ¿Qué umbral indica que una columna
> aporta o no información al modelo?

Mientras llega la respuesta sí se pueden implementar Q1, mediana, Q3, IQR, límites
de outlier y porcentaje de outliers. **No etiquetar ninguna fórmula tentativa como
`IQRratio`.**

### Puntos administrativos pendientes

1. Fecha y hora exactas en Interactiva.
2. Convención de nombre y si se adjunta el dataset/reporte HTML o solo los dos
   archivos exigidos.
3. Si existe una rúbrica o instrucción de citación no incluida en los archivos.

### Decisiones ya resueltas por el material

- EDA automático: `ydata-profiling` con `ProfileReport`,
  `to_notebook_iframe()` y `to_file()`.
- Multicolinealidad: VIF manual con regresión lineal auxiliar,
  `VIF_j = 1/(1-R_j²)`.
- Umbrales de clase: VIF = 1 nulo; 1–5 tolerable; 5–10 alto; ≥10 severo.
- Clasificadores vistos: KNN activo; SVC y Random Forest como alternativas.
- Evaluación de clasificación: accuracy, reporte de clasificación y matriz de
  confusión; el programa del curso también exige precisión, sensibilidad y F1.

### Dataset acordado por el equipo

**Telco Customer Churn**, copia concreta de Kaggle:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

- Archivo esperado: `WA_Fn-UseC_-Telco-Customer-Churn.csv`.
- Unidad de análisis: un cliente de telecomunicaciones.
- Tamaño esperado: 7.043 filas y 21 columnas totales.
- Clasificación binaria; target `Churn` (`Yes`/`No`).
- Clase positiva esperada: 1.869 clientes, aproximadamente 26,5%.
- Pregunta de negocio: **con la información disponible al cierre del mes, predecir
  qué clientes tienen mayor riesgo de abandonar el servicio en el siguiente periodo
  para priorizar acciones de retención.**
- Instante de predicción: cierre del periodo, antes de observar el abandono.
- `customerID` se conserva solo para trazabilidad y se excluye de `X`.
- `Churn` se separa de las predictoras antes de cualquier transformación.

Trabajo de calidad que debe verificarse sobre la copia descargada:

- convertir `TotalCharges` de texto a numérica y cuantificar espacios/nulos;
- comprobar duplicados de fila y unicidad de `customerID`;
- tratar `SeniorCitizen` como binaria, no como magnitud continua;
- conservar `No internet service` y `No phone service` como estados válidos;
- separar numéricas, binarias y nominales antes del encoding;
- auditar correlación/VIF entre `tenure`, `MonthlyCharges` y `TotalCharges`;
- medir el desbalance y no interpretar accuracy de forma aislada.

Límite de interpretación: el dataset es académico/ficticio. El modelo estima
riesgo de churn; no demuestra que una intervención de retención cause permanencia.
El CSV raw no se versionará hasta aclarar si el docente exige adjuntarlo y porque la
página de Kaggle atribuye los datos a sus autores originales.

## 5. Contrato experimental

### Unidad y partición

- Una fila debe representar una unidad independiente y documentada.
- Separar `X` e `y` y ejecutar una única partición reproducible.
- Para clasificación: `test_size=0.20`, `random_state=42`, `stratify=y`, salvo
  instrucción distinta del profesor.
- Guardar los mismos índices de train/test para ambos experimentos.
- El test queda bloqueado hasta la evaluación final.

### Variante A — “sucia”, mínimamente viable

Solo permite operaciones necesarias para que el estimador acepte los datos:

- corregir tipos que impiden leer/modelar;
- retirar target de `X` y cualquier fuga indiscutible;
- imputar únicamente si el modelo no admite nulos;
- codificar categóricas a números;
- no escalar, transformar asimetrías ni eliminar variables por calidad, salvo
  imposibilidad técnica documentada.

### Variante B — limpia y preprocesada

Parte exactamente del mismo train/test e incorpora decisiones aprendidas solo en train:

- reglas de tipos, duplicados y categorías;
- imputación justificada;
- tratamiento justificado de outliers/asimetrías;
- one-hot/label/binary según semántica;
- correlación y multicolinealidad;
- escalamiento compatible con distribución y estimador;
- exclusión de IDs, constantes, fugas o redundancias justificadas.

### Modelo fijo recomendado

Para mantener máxima fidelidad con el código de clase: **KNN de clasificación con
`n_neighbors=7`** en ambas variantes:

```python
KNeighborsClassifier(n_neighbors=7)
```

KNN hace visible el efecto del escalamiento porque calcula distancias; el material
lo identifica expresamente como sensible a escala. No cambiar algoritmo,
hiperparámetros, split o umbral entre A y B para forzar una mejora. Si se hace
validación cruzada o ajuste, debe definirse un único protocolo dentro de train y
aplicarse simétricamente. SVC y Random Forest quedan como ensayos de trabajo, no
como resultados mezclados con la comparación oficial.

### Métricas para clasificación desbalanceada

- Primaria: **F1 de la clase positiva `Churn=Yes`**, fijada antes de entrenar.
- Secundarias: accuracy, precision y recall/sensibilidad de la clase positiva.
- Evidencia visual obligatoria: matriz de confusión.
- Extensión opcional, claramente etiquetada: balanced accuracy y curva
  precision-recall; no deben desplazar las métricas vistas en clase.
- Accuracy nunca se interpreta sola: con 84,5% de sesiones sin compra, un baseline
  trivial puede aparentar buen desempeño.

Tabla final mínima:

| Variante | Accuracy | Precision + | Recall + | F1 + (primaria) | Tiempo |
|---|---:|---:|---:|---:|---:|
| Mínima | pendiente | pendiente | pendiente | pendiente | pendiente |
| Limpia | pendiente | pendiente | pendiente | pendiente | pendiente |

## 6. Receta técnica alineada con la clase

Imports base:

```python
import category_encoders as ce
from ydata_profiling import ProfileReport

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler, RobustScaler
```

### Orden correcto

1. Conservar la fuente raw sin modificar y auditar esquema, tipos, duplicados,
   imposibles, IDs y disponibilidad temporal.
2. El material permite antes del split únicamente correcciones deterministas que no
   aprenden distribuciones: duplicados exactos, strings/formato, tipos, IDs y filas
   inequívocamente corruptas. Documentar cada una.
3. Ejecutar `train_test_split(..., test_size=0.20, random_state=42, stratify=y)`.
4. Aprender imputación, agrupación de categorías, encoding, selección y escaladores
   solo con train; aplicar `transform` a test.
5. Ejecutar EDA manual y automático sobre una copia de train que incluya el target:

```python
eda_train = X_train.copy()
eda_train["Churn"] = y_train
profile = ProfileReport(eda_train, title="EDA automático - train")
profile.to_notebook_iframe()
profile.to_file("artifacts/auto_eda/eda_train.html")
```

El iframe puede no quedar legible en el PDF. Por eso el notebook debe incluir además
una tabla breve de hallazgos del reporte y su contraste autoral con el EDA manual.

### Decisión de transformación por tipo

| Situación | Técnica de clase | Regla para el proyecto |
|---|---|---|
| Numérica con NaN simétrica | media | Ajustar solo en train. |
| Numérica con sesgo/outliers | mediana | Ajustar solo en train. |
| Categórica con NaN | moda o `"Desconocido"` | No crear categoría con información del test. |
| Nominal de baja cardinalidad | One-Hot | `handle_unknown="ignore"`. |
| Ordinal real | mapeo/ordinal | No usar orden si el dominio no lo respalda. |
| Nominal de cardinalidad alta | `BinaryEncoder` | Considerarlo solo si reduce columnas de forma material. |
| Numérica acotada sin outliers altos | MinMaxScaler | Rango [0,1]. |
| Aproximadamente simétrica | StandardScaler | Media 0, desviación 1. |
| Outliers extremos | RobustScaler | Basado en mediana y cuartiles. |
| Positiva muy sesgada, con ceros | `log10(x + 1)` | Extensión segura del ejemplo de clase. |

Para Telco Customer Churn, el plan inicial por columna es:

- `Churn`: label binario `No=0`, `Yes=1`; nunca permanece dentro de `X`.
- `customerID`: excluir del modelo, conservar solo para auditoría.
- `SeniorCitizen`: binaria 0/1.
- `Partner`, `Dependents`, `PhoneService` y `PaperlessBilling`: binarias
  `No=0`, `Yes=1`.
- `gender`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`,
  `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`
  y `PaymentMethod`: One-Hot con categorías desconocidas toleradas.
- `tenure`, `MonthlyCharges` y `TotalCharges`: numéricas; decidir Standard o Robust
  usando solo la distribución de train.
- `BinaryEncoder` de alta cardinalidad se evalúa pero, salvo evidencia distinta al
  descargar, se descarta porque las categorías de Telco tienen baja cardinalidad.
- No forzar Label Encoding en predictoras nominales: crearía un orden artificial.

### Correlación y VIF exactamente como en clase

- Calcular Pearson y Spearman sobre train. Si Spearman supera materialmente a
  Pearson, investigar relación no lineal u outliers.
- Un umbral operativo como `|r| >= 0.95` debe declararse como decisión del equipo,
  no como regla universal del profesor.
- Elegir qué variable retirar por costo de obtención, nulos e interpretabilidad.
- Calcular cada VIF mediante una `LinearRegression` de `X_j` contra las demás:
  `VIF_j = 1/(1-R_j²)`; no hace falta `statsmodels`.
- Interpretar con los umbrales de clase: 1; (1,5); [5,10); ≥10.
- Mitigar VIF alto con retiro/unión de variables; PCA o regularización solo como
  extensiones si pueden defenderse. No aplicar VIF ciegamente a todas las dummies.

`Pipeline` y `ColumnTransformer` no reemplazan los conceptos de clase: se usan para
garantizar que cada `fit` ocurra solo sobre train y que ambas variantes sean
reproducibles.

Antipatrones prohibidos:

- `fit` o `fit_transform` sobre train+test.
- Escalar/codificar todo el dataframe antes del split.
- Usar el target o variables posteriores al evento como predictores.
- Eliminar columnas con un umbral no declarado.
- Aplicar `log(x)` a ceros/negativos sin una transformación válida y justificada.
- Usar label encoding sobre categorías nominales creando orden artificial.
- Calcular VIF sobre todas las dummies sin tratar la trampa de variables ficticias.
- Mirar repetidamente el test para decidir el pipeline.

## 7. Arquitectura del notebook final

Cada bloque de texto marcado **AUTORAL** debe ser redactado desde cero por el equipo.

1. **Portada y autores** — nombres, materia, docente, fecha. **AUTORAL**
2. **Objetivo y contexto de negocio** — problema, usuario de la predicción e instante de uso. **AUTORAL**
3. **Dataset** — fuente, DOI/URL, licencia, versión, unidad de análisis, target. **AUTORAL**
4. **Contrato experimental** — clasificación/regresión, split, semilla, modelo y métricas. **AUTORAL**
5. **Carga y auditoría inicial** — forma, tipos, nulos, duplicados, cardinalidades, target.
6. **Partición sin fuga** — creación y bloqueo de train/test.
7. **EDA manual de train** — media/mediana/moda, varianza/desviación/rango,
   Q1/Q2/Q3/percentiles, IQR, límites 1,5·IQR, `IQRratio` confirmado,
   distribuciones y target.
8. **EDA automático de train** — `ydata-profiling`, configuración, reporte HTML
   de trabajo y hallazgos visibles en el notebook/PDF.
9. **Comparación EDA manual vs. automático** — tabla de coincidencias, diferencias y decisiones. **AUTORAL**
10. **Pipeline mínimo** — transformaciones imprescindibles y justificación. **AUTORAL**
11. **Pipeline limpio** — limpieza, encoding, Pearson/Spearman, VIF manual y scaling. **AUTORAL**
12. **Entrenamiento del mismo modelo** — configuración compartida y evidencia de igualdad.
13. **Evaluación comparativa** — métricas, matrices/curvas, delta absoluto y relativo.
14. **Análisis de resultados** — explicación honesta de mejora, empate o deterioro. **AUTORAL**
15. **Conclusiones, límites y trabajo futuro**. **AUTORAL**
16. **Referencias** — dataset, librerías y fuentes académicas.
17. **Anexo reproducible** — versiones, semilla, checksum y tiempo de ejecución.

## 8. Plan por fases

### Fase 0 — Cerrar contrato académico y técnico

Implementar:

- Resolver el `IQRratio` y los tres puntos administrativos de la sección 4.
- Elegir dataset y registrar URL, DOI/licencia, fecha y checksum.
- Escribir entre los tres la pregunta de negocio y el instante de predicción.
- Fijar target, tarea, split, KNN(7) y F1 positiva como protocolo principal, salvo
  indicación distinta del docente.

Referencias: PDF pp. 2–5; página oficial del dataset elegido.

Verificación:

- Una hoja de decisiones con aprobación de los tres.
- Ninguna variable predictora requiere información posterior al instante de predicción.
- Todos pueden explicar el problema y cada métrica sin leer este plan.

Guardias: no empezar EDA/modelado con decisiones abiertas; no escoger el dataset
solo porque promete una accuracy alta.

### Fase 1 — Entorno reproducible y adquisición

Implementar:

```powershell
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe pandas scikit-learn scipy matplotlib seaborn category-encoders==2.10.0 ydata-profiling==4.18.4 jupyterlab ipykernel nbconvert
```

Estas versiones son compatibles con Python 3.12 al momento de la auditoría. Aunque
`ydata-profiling` fue renombrado externamente, se conserva ese paquete/import porque
es la API exacta enseñada; no migrar a `fg-data-profiling` a mitad de la entrega.
Congelar todas las versiones instaladas y registrar checksum del dataset. No
modificar el CSV/XLSX original; trabajar con copias o transformaciones en memoria.

Estructura de trabajo propuesta:

```text
data/raw/                 # fuente inmutable, no necesariamente entregable
artifacts/auto_eda/       # reporte automático de trabajo
Informe_Teorico_Practico_1.ipynb
requirements-lock.txt
PLAN_TECNICO_ENTREGA.md
```

Verificación:

- Kernel del proyecto visible y apuntando a `.venv`.
- Imports pasan.
- Dataset carga desde una ruta relativa.
- Shape, columnas, dtypes y checksum quedan registrados.

Guardias: no instalar dependencias globales; no guardar rutas absolutas; no
sobrescribir el archivo raw.

### Fase 2 — Auditoría, split y EDA manual

Implementar:

- Auditoría de esquema y disponibilidad temporal de cada variable.
- Aplicar solo limpieza determinista pre-split autorizada por la clase; split único
  antes de imputación, scaling, selección o EDA que guíe decisiones.
- Estadística descriptiva de train: media/mediana/moda, varianza/desviación/rango/IQR,
  cuantiles, límites 1,5·IQR y `IQRratio` confirmado.
- Histogramas, boxplots, barras de categorías y distribución del target.
- Correlación Pearson/Spearman según evidencia y análisis inicial de colinealidad.

Referencias: enunciado pp. 6–7; `EDA.ipynb`; tramo final de
`AdquisicionLimpiezaDatos.pdf`.

Verificación:

- Índices train/test disjuntos y suma de tamaños correcta.
- Proporción de clases documentada en ambos conjuntos.
- Toda cifra que decida una transformación proviene de train.
- Cada visual responde una pregunta y tiene título/ejes/unidades.

Guardias: no usar test en `describe`, correlaciones o gráficos decisorios; no borrar
outliers automáticamente.

### Fase 3 — EDA automático y contraste

Implementar:

- Ejecutar `ProfileReport(eda_train, ...)` únicamente sobre train.
- Generar iframe para el notebook y HTML como artefacto de trabajo.
- Extraer alertas pertinentes, no pegar todo el reporte sin criterio.
- Crear tabla manual vs. automático: hallazgo, coincidencia, diferencia, decisión.

Referencias: enunciado p. 7; celdas 13–15 de `EDA.ipynb`; API oficial de
`ydata-profiling`.

Verificación:

- Reporte abre y corresponde exactamente al train.
- Cada decisión técnica puede rastrearse a evidencia manual, automática o de dominio.

Guardias: el EDA automático no reemplaza el manual ni decide por el equipo.

### Fase 4 — Construir los dos pipelines

Implementar:

- Pipeline mínimo y pipeline limpio con `ColumnTransformer` + `Pipeline`.
- Confirmar salida totalmente numérica.
- Registrar variables eliminadas y razón: ID, fuga, constante, Pearson/Spearman o
  VIF manual.
- Mantener el mismo objeto/fábrica de estimador y los mismos hiperparámetros.

Referencias: enunciado pp. 6 y 8; `limpiezaDatos.ipynb` celdas 53–73;
`aplicarModeloML(2).ipynb`.

Verificación:

- Cada pipeline hace `fit` solo con train y `transform/predict` con test.
- Categorías nuevas no rompen el pipeline.
- No quedan NaN/inf ni columnas no numéricas a la entrada del estimador.
- Prueba programática de igualdad de clase e hiperparámetros del modelo.

Guardias: no comparar modelos diferentes; no alterar el split; no usar el test para
elegir columnas o umbrales.

### Fase 5 — Evaluación y redacción autoral

Implementar:

- Evaluar una vez sobre el holdout común.
- Tabla comparativa, `classification_report` y matriz de confusión.
- Calcular delta absoluto y relativo de la métrica primaria.
- Los tres redactan análisis, conclusiones, limitaciones y justificaciones con sus
  propias palabras.

Referencias: PDF p. 8; documentación oficial de métricas de scikit-learn.

Verificación:

- Resultados se pueden regenerar con Restart Kernel + Run All.
- No se afirma causalidad a partir de correlación.
- Si no mejora, se reporta y explica sin cambiar el protocolo a posteriori.
- Cada integrante puede defender verbalmente código y decisiones.

Guardias: no optimizar contra test; no escribir primero la conclusión deseada.

### Fase 6 — Integración y entrega

Implementar:

- Revisar notebook completo desde kernel limpio.
- Eliminar celdas de depuración, rutas personales, errores y salidas gigantes.
- Ejecutar con fallo duro:

```powershell
.venv\Scripts\python.exe -m nbconvert --execute --to notebook --inplace Informe_Teorico_Practico_1.ipynb
.venv\Scripts\python.exe -m nbconvert --to html Informe_Teorico_Practico_1.ipynb
```

- Abrir el HTML en Edge/Chrome e imprimir a PDF si no se configura una ruta de PDF
  reproducible de nbconvert.
- Comparar visualmente notebook y PDF página por página.

Verificación final:

- Exactamente los dos entregables pedidos en una carpeta de entrega limpia.
- PDF legible, sin gráficos cortados ni texto fuera de página.
- Notebook conserva todos los outputs que aparecen en el PDF.
- Búsqueda de rutas absolutas, nombres de usuario, secretos y celdas con error: cero.
- Copia de respaldo fuera de la carpeta de entrega.

Guardias: no usar `--allow-errors`; no exportar antes del Run All definitivo; no
entregar archivos auxiliares sin confirmación del profesor.

## 9. Reparto equilibrado para tres integrantes

Reparto revisado el 31 de agosto de 2026: el EDA completo (manual y automático)
queda en una sola persona y el preprocesamiento completo en otra, porque ambos
frentes tienen carga comparable y separarlos por herramienta la desequilibraba.

| Integrante | Propiedad principal | Evidencia que entrega | Revisión cruzada |
|---|---|---|---|
| 1 — `srodrigub1` — Negocio/datos/EDA | Problema, fuente, diccionario, auditoría, split, estadística, `IQRratio`, visuales, ProfileReport y contraste manual vs. automático | Secciones 2–9 y checklist de calidad | Revisa métricas/modelo del 3 |
| 2 — `Pacha-e` — Preprocesamiento/integración | Pipeline mínimo, pipeline limpio, encoding, Pearson/Spearman, VIF, scaling y tabla de decisiones por columna | Secciones 10–11 y 16–17; notebook/PDF integrados | Revisa EDA del 1 |
| 3 — `Ang3l1485` — Modelado/comparación | KNN fijo en ambas variantes, métricas, matrices y comparación | Secciones 12–15 | Revisa leakage/pipelines del 2 |

Responsabilidad compartida no delegable:

- Los tres aprueban el contrato de la fase 0.
- Cada autor redacta la justificación de sus propias decisiones.
- Los tres revisan análisis y conclusiones finales.
- Cada bloque necesita autor y revisor distintos.

Protocolo para evitar conflictos del `.ipynb`:

1. `Pacha-e` custodia la copia maestra durante la integración.
2. Cada dueño trabaja en un rango de secciones acordado y entrega celdas probadas.
3. Solo una persona integra a la vez; después ejecuta desde la primera celda.
4. Cada traspaso incluye: inputs, outputs esperados, dependencias y pruebas.

## 10. Secuencia de sesiones

| Sesión | Resultado obligatorio |
|---|---|
| 0 — 45–60 min | Preguntas al profesor, dataset y contrato experimental cerrados. |
| 1 — 2 h | Entorno, descarga trazable, diccionario, checksum y split congelado. |
| 2 — 3 h en paralelo | EDA manual, EDA automático y prototipos de ambos pipelines. |
| 3 — 2–3 h | Pipelines integrados, modelo común, pruebas anti-leakage y métricas. |
| 4 — 2 h | Redacción autoral, revisión cruzada y defensa oral interna. |
| 5 — 1–2 h | Run All, exportación, auditoría visual y paquete final. |

## 11. Checklist de calidad final

### Integridad académica

- [ ] La prosa final fue escrita por estudiantes, no copiada de este plan.
- [ ] Cada integrante entiende todo comando que aparece en el notebook.
- [ ] Las fuentes externas están citadas y no hay texto sin atribución.

### Datos y fuga

- [ ] Dataset/version/checksum registrados.
- [ ] Target fuera de `X`.
- [ ] Split anterior a transformaciones aprendidas.
- [ ] Test sin participar en EDA decisorio ni `fit`.
- [ ] Variables post-evento/IDs/proxies revisadas explícitamente.

### EDA y preprocesamiento

- [ ] Tendencia central, dispersión, posición e `IQRratio` completos.
- [ ] Visualizaciones legibles e interpretadas.
- [ ] EDA manual comparado explícitamente con el automático de clase.
- [ ] Encoding, correlación, multicolinealidad y scaling justificados.
- [ ] Matriz transformada totalmente numérica, finita y sin nulos.

### Experimento

- [ ] Mismos índices, modelo, hiperparámetros y métricas en ambas variantes.
- [ ] Métrica primaria fijada antes de mirar test.
- [ ] Comparación incluye más que accuracy.
- [ ] Resultado no fue manipulado para obligar una mejora.

### Reproducibilidad y entrega

- [ ] Ruta relativa y semilla fija.
- [ ] Versiones del entorno registradas.
- [ ] Restart Kernel + Run All sin errores.
- [ ] PDF coincide con la última ejecución.
- [ ] Carpeta final contiene solo `.ipynb` y `.pdf`, salvo orden distinta del docente.

## 12. Registro de riesgos

| Riesgo | Severidad | Mitigación |
|---|---|---|
| Prosa generada por IA | Crítica | Bloques AUTORAL, revisión de los tres y reescritura desde comprensión. |
| Fórmula `IQRratio` incorrecta | Alta | Obtener definición y umbral directamente del docente antes de programar/interpretar. |
| Perfil automático invisible en el PDF | Alta | Generar HTML de trabajo y trasladar hallazgos/tablas esenciales al notebook. |
| Data leakage | Crítica | Split primero, pipelines, auditoría temporal y test bloqueado. |
| Accuracy engañosa por desbalance | Alta | Métrica primaria sensible al desbalance y matriz de confusión. |
| Notebook imposible de reproducir | Alta | `.venv`, lock, rutas relativas, checksum y Run All. |
| Conflictos de notebook | Media | Integrador único y propiedad de secciones. |
| PDF incompleto/cortado | Media | Exportar temprano una prueba y auditar visualmente el final. |
| No mejora el dataset limpio | Media | Reportar el resultado real y analizarlo; no forzar la hipótesis. |

## 13. Documentación primaria consultada

- Enunciado local: [`informeTeoricoPrac1.pdf`](./informeTeoricoPrac1.pdf).
- Material local: `presentacionDelCurso (1).pdf`, `Fundamentos (1).pdf`,
  `lecturaCasosCicloVida (1).pdf`, `ambienteDesarrollo (1).pdf`,
  `AdquisicionLimpiezaDatos.pdf`, `limpiezaDatos.ipynb`, `EDA.ipynb` y
  `aplicarModeloML(2).ipynb` en la carpeta padre.
- Kaggle, Telco Customer Churn:
  https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- IBM, descripción del dataset de churn:
  https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113
- UCI Bank Marketing: https://archive.ics.uci.edu/dataset/222/bank+marketing
- Scikit-learn, fuga y pipelines: https://scikit-learn.org/stable/common_pitfalls.html
- Scikit-learn, tipos mixtos: https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html
- Scikit-learn, split: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
- Scikit-learn, evaluación: https://scikit-learn.org/stable/modules/model_evaluation.html
- PyPI, `ydata-profiling`: https://pypi.org/project/ydata-profiling/
- PyPI, `category-encoders`: https://pypi.org/project/category-encoders/
- NIST, coeficiente cuartílico de dispersión:
  https://www.itl.nist.gov/div898/software/dataplot/refman2/auxillar/qcd.htm

## 14. Próximo movimiento recomendado

Próximos bloqueos reales:

1. Confirmación docente de la fórmula y umbral de `IQRratio`.
2. Fecha/hora exacta y requisitos adicionales visibles en Interactiva.
3. Aceptación de la invitación de GitHub pendiente para `Ang3l1485`.
4. Descargar la copia exacta de Kaggle, verificar esquema y registrar SHA-256.

El dataset, problema, target, instante de predicción, modelo principal y reparto de
roles ya están cerrados.
