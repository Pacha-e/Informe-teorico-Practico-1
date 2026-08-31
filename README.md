# Informe Teórico Práctico 1 — Telco Customer Churn

Proyecto de **Fundamentos de Aprendizaje Automático** para estudiar cómo cambia el
desempeño de un mismo clasificador al comparar un dataset mínimamente procesado con
una versión limpiada y preprocesada de forma completa.

## Problema acordado

> Con la información disponible al cierre del mes, predecir qué clientes tienen
> mayor riesgo de abandonar el servicio en el siguiente periodo para priorizar
> acciones de retención.

- Dataset: [Telco Customer Churn en Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Target: `Churn` (`Yes`/`No`)
- Tarea: clasificación binaria
- Modelo común: `KNeighborsClassifier(n_neighbors=7)`
- Métrica primaria: F1 de `Churn=Yes`
- Split: 80/20 estratificado, `random_state=42`

El contrato completo está en [`docs/CONTRATO_PROBLEMA.md`](docs/CONTRATO_PROBLEMA.md)
y la planeación académica en
[`PLAN_TECNICO_ENTREGA.md`](PLAN_TECNICO_ENTREGA.md).

## Equipo

| Integrante GitHub | Responsabilidad principal |
|---|---|
| `srodrigub1` | Negocio, adquisición, auditoría y EDA completo (manual y automático) |
| `Pacha-e` | Preprocesamiento: pipeline mínimo y pipeline limpio |
| `Ang3l1485` | Entrenamiento del KNN y comparación de ambas variantes |

Reparto revisado el 31 de agosto de 2026 para que el EDA y el preprocesamiento no
recaigan en la misma persona; queda registrado en [`docs/DECISIONES.md`](docs/DECISIONES.md).

`Pacha-e` custodia el notebook maestro y la integración. Cada bloque requiere
revisión de una persona distinta de su autora.

## Plan operativo en GitHub

Todo el trabajo está agrupado en el hito
[Informe Teórico Práctico 1](https://github.com/Pacha-e/Informe-teorico-Practico-1/milestone/1):

- decisiones y datos: [#1](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/1) y [#2](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/2);
- EDA manual y automático: [#3](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/3) y [#4](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/4);
- pipelines mínimo y limpio: [#5](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/5) y [#6](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/6);
- modelado, integración y entrega: [#7](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/7), [#8](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/8) y [#9](https://github.com/Pacha-e/Informe-teorico-Practico-1/issues/9).

## Preparación local

Requisitos: Python 3.12 y [`uv`](https://docs.astral.sh/uv/).

Para la incorporación completa y el reparto del primer día, consultar
[`docs/GUIA_ARRANQUE_EQUIPO.md`](docs/GUIA_ARRANQUE_EQUIPO.md).

```powershell
uv sync --locked
uv run python scripts/download_data.py
uv run python scripts/verify_data.py
uv run jupyter lab
```

El descargador obtiene la copia concreta de Kaggle. El CSV raw queda en `data/raw/`
y no se versiona. Nunca guardar `kaggle.json`, tokens ni credenciales en el repo.

## Flujo de trabajo

1. Elegir una issue no bloqueada y anunciarla.
2. Crear rama desde `main`: `feat/<numero>-<slug>` o `docs/<numero>-<slug>`.
3. Hacer cambios pequeños con Conventional Commits.
4. Abrir PR enlazando `Closes #N`.
5. Obtener una revisión cruzada y pasar CI.
6. Integrar mediante squash merge. Nadie trabaja directamente en `main`.

Detalles: [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Entregables oficiales

- `Informe_Teorico_Practico_1.ipynb`, ejecutado sin errores.
- `Informe_Teorico_Practico_1.pdf`, exportado de esa misma ejecución.

La narrativa académica debe ser escrita y defendida por los estudiantes. La IA se
usa como apoyo de programación, no como autora de justificaciones, análisis o
conclusiones.
