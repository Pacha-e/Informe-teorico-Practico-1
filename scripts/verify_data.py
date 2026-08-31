"""Verifica que el CSV local corresponde al dataset acordado por el equipo."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
EXPECTED_COLUMNS = [
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "Dependents",
    "tenure",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
    "Contract",
    "PaperlessBilling",
    "PaymentMethod",
    "MonthlyCharges",
    "TotalCharges",
    "Churn",
]
EXPECTED_ROWS = 7_043
EXPECTED_POSITIVES = 1_869


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"No existe {DATA_PATH}. Ejecuta primero scripts/download_data.py."
        )

    data = pd.read_csv(DATA_PATH, dtype=str, keep_default_na=False)
    errors: list[str] = []

    if data.columns.tolist() != EXPECTED_COLUMNS:
        errors.append("el orden o los nombres de las 21 columnas no coinciden")
    if len(data) != EXPECTED_ROWS:
        errors.append(f"se esperaban {EXPECTED_ROWS} filas y llegaron {len(data)}")
    if data["customerID"].duplicated().any():
        errors.append("customerID contiene duplicados")
    if set(data["Churn"].unique()) != {"Yes", "No"}:
        errors.append("Churn no contiene exactamente las clases Yes y No")

    positives = int((data["Churn"] == "Yes").sum())
    if positives != EXPECTED_POSITIVES:
        errors.append(
            f"se esperaban {EXPECTED_POSITIVES} positivos y llegaron {positives}"
        )

    for column in ("SeniorCitizen", "tenure", "MonthlyCharges"):
        if pd.to_numeric(data[column], errors="coerce").isna().any():
            errors.append(f"{column} contiene valores no numéricos")

    total_charges = pd.to_numeric(data["TotalCharges"], errors="coerce")
    blank_total_charges = int(total_charges.isna().sum())

    if errors:
        raise ValueError("Dataset inválido:\n- " + "\n- ".join(errors))

    print(f"OK: {data.shape[0]} filas x {data.shape[1]} columnas")
    print(f"Churn=Yes: {positives} ({positives / len(data):.2%})")
    print(f"TotalCharges no convertibles o vacíos: {blank_total_charges}")
    print(f"SHA-256: {sha256(DATA_PATH)}")


if __name__ == "__main__":
    main()
