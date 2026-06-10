from pathlib import Path

base = Path("autopilot_datasets")
base.mkdir(exist_ok=True)

subfolders = ["raw", "processed", "models"]

for folder in subfolders:
    (base / folder).mkdir(exist_ok=True)

files = {
    "raw/data.csv": "",
    "processed/clean.csv": "",
    "models/model.pkl": ""
}

for file_path, content in files.items():
    path = base / file_path
    path.write_text(content)

print("Files found:\n")
for file in base.glob("*/*"):
    print(file)

print("\nFile Information:\n")
for file in base.glob("*/*"):
    print(f"Name   : {file.name}")
    print(f"Parent : {file.parent}")
    print(f"Exists : {file.exists()}")
    print("-" * 30)