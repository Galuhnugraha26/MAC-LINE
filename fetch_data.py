from pathlib import Path
from ucimlrepo import fetch_ucirepo

dataset = fetch_ucirepo(id=601)

df = dataset.data.features.copy()
df["Machine failure"] = dataset.data.targets["Machine failure"]

expected = {
    "Type",
    "Air temperature",
    "Process temperature",
    "Rotational speed",
    "Torque",
    "Tool wear",
    "Machine failure",
}

assert len(df) == 10000, "Unexpected number of records"
assert set(df.columns) == expected, "Unexpected dataset columns"
assert not df.isna().any().any(), "Dataset contains missing values"

Path("data").mkdir(exist_ok=True)
df.to_csv("data/ai4i2020.csv", index=False)

print("Dataset downloaded and validated.")
print("Records:", len(df))
print("Columns:", list(df.columns))
print("Failure distribution:")
print(df["Machine failure"].value_counts())
