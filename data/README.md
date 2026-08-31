# Datos del proyecto

## Fuente canónica

- Dataset: **Telco Customer Churn**.
- Propietario en Kaggle: `blastchar`.
- Identificador: `blastchar/telco-customer-churn`.
- Archivo esperado: `WA_Fn-UseC_-Telco-Customer-Churn.csv`.
- Página: <https://www.kaggle.com/datasets/blastchar/telco-customer-churn>

El CSV crudo no se versiona en Git. Cada integrante debe obtener su copia con:

```powershell
uv run python scripts/download_data.py
uv run python scripts/verify_data.py
```

`download_data.py` no sobrescribe silenciosamente un archivo distinto. La
verificación exige 7.043 filas, las 21 columnas esperadas, identificadores
únicos y la codificación `Yes`/`No` de la variable objetivo.

Snapshot verificado durante el setup del 31 de agosto de 2026:

- SHA-256: `88be4b93fbe0cc83421af1c503794c97c342eca914c1576db7c276e61d61358a`.
- Dimensión: 7.043 filas x 21 columnas.
- `Churn=Yes`: 1.869 observaciones (26,54 %).
- `TotalCharges` vacío/no convertible: 11 observaciones.

## Trazabilidad

Cada ejecución de `verify_data.py` imprime el SHA-256 del CSV. El equipo debe
registrar ese valor en el notebook y comprobar que los tres integrantes usan la
misma copia.

## Uso y licencia

El dataset se usará únicamente para esta actividad académica. Antes de una
redistribución o publicación fuera del curso, el equipo debe revisar en Kaggle
las condiciones vigentes de uso; por esa razón el archivo crudo permanece
fuera del repositorio.
