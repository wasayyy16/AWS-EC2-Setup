import pandas as pd
import os
import joblib
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Paths
DATA_PATH = "/mnt/ml-data/datasets/raw.csv"
MODEL_DIR = "/mnt/ml-data/models/"
LOG_DIR = "/mnt/ml-data/logs/"
LOG_FILE = os.path.join(LOG_DIR, "training_metrics.txt")

# Ensure directories exist
os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

def run_pipeline():
    print("Loading data...")
    # Adjust column names based on UCI Adult dataset structure if needed
    # Assuming standard CSV format for this example
    try:
        df = pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: File not found at {DATA_PATH}")
        return

    # Basic Preprocessing (Simulated for brevity - customize for Adult dataset)
    # Dropping non-numeric for simplicity in this template
    df = df.select_dtypes(include=['number']).dropna()
    
    # Assuming last column is target
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    # Models
    models = {
        "RandomForest": RandomForestClassifier(),
        "LogisticRegression": LogisticRegression()
    }

    best_model_name = ""
    best_acc = 0
    best_model_obj = None

    log_entries = []

    print("Training models...")
    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"Model: {name}\nAccuracy: {acc:.4f}\nTimestamp: {timestamp}\n----------------"
        print(entry)
        log_entries.append(entry)

        if acc > best_acc:
            best_acc = acc
            best_model_name = name
            best_model_obj = model

    # Save Best Model
    save_path = os.path.join(MODEL_DIR, f"best_model_{best_model_name}.pkl")
    joblib.dump(best_model_obj, save_path)
    print(f"Best model saved to: {save_path}")

    # Log Metrics
    with open(LOG_FILE, "a") as f:
        for entry in log_entries:
            f.write(entry + "\n")
    print(f"Metrics logged to: {LOG_FILE}")

if __name__ == "__main__":
    run_pipeline()
