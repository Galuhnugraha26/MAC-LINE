from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


DATA_PATH = Path("data/ai4i2020.csv")

FEATURES = [
    "Type",
    "Air temperature",
    "Process temperature",
    "Rotational speed",
    "Torque",
    "Tool wear",
]

TARGET = "Machine failure"

df = pd.read_csv(DATA_PATH)

X = df[FEATURES]
y = df[TARGET]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "type",
            OneHotEncoder(handle_unknown="ignore"),
            ["Type"],
        ),
        (
            "numeric",
            "passthrough",
            FEATURES[1:],
        ),
    ]
)

classifier = RandomForestClassifier(
    n_estimators=100,
    max_depth=8,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1,
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier", classifier),
    ]
)

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("ModelServe-AI4I")

with mlflow.start_run(run_name="random-forest-baseline"):

    mlflow.log_params({
        "model": "RandomForestClassifier",
        "n_estimators": 100,
        "max_depth": 8,
        "class_weight": "balanced",
        "test_size": 0.2,
        "random_state": 42,
        "dataset": "UCI AI4I 2020",
    })

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(
            y_test, predictions, zero_division=0
        ),
        "recall": recall_score(
            y_test, predictions, zero_division=0
        ),
        "f1_score": f1_score(
            y_test, predictions, zero_division=0
        ),
    }

    mlflow.log_metrics(metrics)
    mlflow.sklearn.log_model(
    sk_model=pipeline,
    name="model",
    skops_trusted_types=["sklearn.tree._tree.Tree"],
)

    Path("model").mkdir(exist_ok=True)
    joblib.dump(pipeline, "model/model.joblib")

    print("\nModelServe training completed.")
    for name, value in metrics.items():
        print(f"{name}: {value:.4f}")

    print("Model saved: model/model.joblib")
    print("Experiment logged to MLflow.")
