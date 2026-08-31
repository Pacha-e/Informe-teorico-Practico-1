# Guía de colaboración

## Estrategia Git

Usamos GitHub Flow:

- `main` contiene solo trabajo revisado e integrado.
- Una rama corta por issue: `feat/12-eda-manual`, `docs/3-contrato-datos`.
- Un PR resuelve una sola issue y usa squash merge.
- No hacer force-push sobre ramas compartidas ni reescribir `main`.

## Convención de commits

Formato: `<tipo>(<alcance>): <descripción>`.

Ejemplos:

```text
docs(datos): documenta procedencia y checksum
feat(eda): agrega estadísticas manuales de train
fix(modelo): evita ajustar el scaler con test
```

## Regla especial para el notebook

El archivo `.ipynb` genera conflictos difíciles de revisar. Por eso:

1. `Pacha-e` mantiene el notebook maestro.
2. Cada integrante desarrolla su bloque en una rama y evita reordenar secciones ajenas.
3. Antes del PR: limpiar ejecuciones fallidas y ejecutar las celdas propias.
4. Solo una PR que toque el notebook se integra a la vez.
5. La siguiente rama actualiza `main` antes de continuar.

## Definición de listo para una PR

- La issue y sus criterios de aceptación están cubiertos.
- No hay rutas absolutas, secretos ni datos raw versionados.
- El código aprende transformaciones solo con train.
- Las cifras y gráficos tienen unidades, etiquetas y fuente.
- Se ejecutó la verificación más cercana al cambio.
- La prosa evaluada fue escrita por el equipo.
- La PR nombra a una persona revisora distinta de la autora.
