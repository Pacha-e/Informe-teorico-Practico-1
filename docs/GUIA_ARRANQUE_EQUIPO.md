# Guía de arranque del equipo

Esta guía permite que cada integrante empiece desde una clonación limpia sin
compartir rutas locales, entornos virtuales ni el CSV crudo.

## 1. Preparar el equipo

```powershell
git clone https://github.com/Pacha-e/Informe-teorico-Practico-1.git
cd Informe-teorico-Practico-1
uv sync --locked
uv run python scripts/download_data.py
uv run python scripts/verify_data.py
uv run python scripts/verify_repo.py
```

El verificador del dataset debe informar 7.043 filas, 21 columnas y el SHA-256
documentado en `data/README.md`. Si el hash es diferente, no se debe continuar
hasta revisar la fuente.

## 2. Reparto inicial

| Integrante | Issues | Notebook de trabajo |
|---|---|---|
| `srodrigub1` | #2, #3 y #4 | `notebooks/work/01_datos_eda_manual.ipynb` |
| `Pacha-e` | #1, #5, #6, #8 y #9 | `notebooks/work/02_preprocesamiento.ipynb` |
| `Ang3l1485` | #7 | `notebooks/work/03_modelado_comparacion.ipynb` |

Reparto revisado el 31 de agosto de 2026: el EDA completo queda en una sola
persona y el preprocesamiento completo en otra.

La invitación pendiente de `Ang3l1485` no bloquea la preparación local: el
repositorio es público y puede clonarlo. Para publicar una rama deberá aceptar
la invitación o trabajar temporalmente desde un fork.

## 3. Empezar una tarea

Siempre partir de `main` actualizado:

```powershell
git switch main
git pull --rebase origin main
git switch -c feat/2-auditoria-datos
```

Cambiar `2-auditoria-datos` por el número y nombre corto de la issue. Usar
`docs/<numero>-<slug>` cuando solo se modifique documentación.

## 4. Evitar conflictos en notebooks

- Nadie salvo `Pacha-e` edita directamente
  `notebooks/Informe_Teorico_Practico_1.ipynb`.
- Cada persona desarrolla y prueba en su notebook dentro de `notebooks/work/`.
- Los reportes HTML de ydata-profiling se guardan en `artifacts/`; no entran a Git.
- Al terminar una issue, el PR explica qué celdas o funciones debe integrar
  `Pacha-e` en el notebook maestro.
- No renombrar columnas ni cambiar el split común sin registrarlo en
  `docs/DECISIONES.md` y discutirlo en la issue correspondiente.

## 5. Antes de abrir un PR

```powershell
uv run python scripts/verify_repo.py
uv run python scripts/verify_data.py
git status
```

Además:

- ejecutar **Restart Kernel and Run All** sobre el notebook modificado;
- revisar que no aparezcan rutas absolutas, credenciales ni el CSV crudo;
- usar un commit descriptivo, por ejemplo
  `feat(eda): completa auditoría inicial del dataset`;
- abrir el PR contra `main`, enlazar la issue y solicitar una revisión.

## 6. Orden recomendado para el primer día

1. Todos ejecutan la preparación local y comparan el SHA-256.
2. `srodrigub1` inicia #2 y encadena #3 y #4 en el mismo notebook.
3. `Pacha-e` entrega #5 y #6 lo antes posible: el modelado depende de ellas.
4. `Ang3l1485` prepara #7 en su notebook local; puede publicar cuando acepte la
   invitación.
5. El equipo hace una sincronización corta y registra bloqueos directamente en
   las issues, no en mensajes aislados.
