"""Descarga de forma reproducible el CSV de Telco Customer Churn desde Kaggle."""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

import kagglehub


DATASET_HANDLE = "blastchar/telco-customer-churn"
EXPECTED_FILENAME = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DESTINATION = PROJECT_ROOT / "data" / "raw" / EXPECTED_FILENAME


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    cache_path = Path(kagglehub.dataset_download(DATASET_HANDLE))
    matches = list(cache_path.rglob(EXPECTED_FILENAME))
    if len(matches) != 1:
        raise RuntimeError(
            f"Se esperaba un único {EXPECTED_FILENAME} en {cache_path}; "
            f"se encontraron {len(matches)}."
        )

    source = matches[0]
    source_hash = sha256(source)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)

    if DESTINATION.exists():
        destination_hash = sha256(DESTINATION)
        if destination_hash != source_hash:
            raise RuntimeError(
                "Ya existe un CSV local con contenido diferente. "
                "Revísalo y elimínalo manualmente si deseas reemplazarlo."
            )
        print(f"Dataset ya sincronizado: {DESTINATION}")
    else:
        shutil.copy2(source, DESTINATION)
        print(f"Dataset copiado en: {DESTINATION}")

    print(f"SHA-256: {source_hash}")


if __name__ == "__main__":
    main()
