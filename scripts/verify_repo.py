"""Comprobaciones rápidas de estructura que no requieren el dataset crudo."""

from __future__ import annotations

import json
import re
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = PROJECT_ROOT / "notebooks" / "Informe_Teorico_Practico_1.ipynb"
REQUIRED_PATHS = [
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "CONTRIBUTING.md",
    PROJECT_ROOT / "pyproject.toml",
    PROJECT_ROOT / "uv.lock",
    PROJECT_ROOT / "docs" / "CONTRATO_PROBLEMA.md",
    PROJECT_ROOT / "docs" / "GUIA_ARRANQUE_EQUIPO.md",
    PROJECT_ROOT / "data" / "README.md",
    PROJECT_ROOT / "scripts" / "download_data.py",
    PROJECT_ROOT / "scripts" / "verify_data.py",
    PROJECT_ROOT / ".github" / "CODEOWNERS",
    PROJECT_ROOT / "notebooks" / "work" / "README.md",
    PROJECT_ROOT / "notebooks" / "work" / "01_datos_eda_manual.ipynb",
    PROJECT_ROOT / "notebooks" / "work" / "02_preprocesamiento.ipynb",
    PROJECT_ROOT / "notebooks" / "work" / "03_modelado_comparacion.ipynb",
    NOTEBOOK,
]
REQUIRED_NOTEBOOK_SECTIONS = [
    "Problema de negocio",
    "comprensión de los datos",
    "Partición de entrenamiento y prueba",
    "EDA manual",
    "EDA automático",
    "Pipeline mínimo",
    "Pipeline limpio",
    "Modelado con KNN",
    "Comparación de resultados",
    "Conclusiones",
]
PORTABLE_FILES = [
    PROJECT_ROOT / "README.md",
    PROJECT_ROOT / "CONTRIBUTING.md",
    *sorted((PROJECT_ROOT / "docs").glob("*.md")),
    NOTEBOOK,
    *sorted((PROJECT_ROOT / "notebooks" / "work").glob("*.ipynb")),
]


def main() -> None:
    missing = [str(path.relative_to(PROJECT_ROOT)) for path in REQUIRED_PATHS if not path.exists()]
    if missing:
        raise FileNotFoundError("Faltan archivos requeridos: " + ", ".join(missing))

    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4:
        raise ValueError("El notebook no usa nbformat 4")

    notebook_text = "\n".join(
        "".join(cell.get("source", [])) for cell in notebook.get("cells", [])
    )
    missing_sections = [
        section for section in REQUIRED_NOTEBOOK_SECTIONS if section not in notebook_text
    ]
    if missing_sections:
        raise ValueError(
            "Faltan secciones del notebook: " + ", ".join(missing_sections)
        )

    for path in sorted((PROJECT_ROOT / "notebooks").rglob("*.ipynb")):
        candidate = json.loads(path.read_text(encoding="utf-8"))
        if candidate.get("nbformat") != 4:
            raise ValueError(f"{path.name} no usa nbformat 4")
        cells_without_id = [
            index
            for index, cell in enumerate(candidate.get("cells", []), start=1)
            if not cell.get("id")
        ]
        if cells_without_id:
            raise ValueError(
                f"{path.name} tiene celdas sin id: {cells_without_id}"
            )

    absolute_path = re.compile(r"[A-Za-z]:\\(?:Users|Universidad)\\", re.IGNORECASE)
    leaks = []
    for path in PORTABLE_FILES:
        if absolute_path.search(path.read_text(encoding="utf-8")):
            leaks.append(str(path.relative_to(PROJECT_ROOT)))
    if leaks:
        raise ValueError("Hay rutas locales no portables en: " + ", ".join(leaks))

    print("OK: estructura, notebook y portabilidad básica verificados")


if __name__ == "__main__":
    main()
