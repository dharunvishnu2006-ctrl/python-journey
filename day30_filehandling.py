from pathlib import Path
import shutil
import glob
import os

base = Path("cloudshield_logs")
base.mkdir(exist_ok=True)
(base / "2025-01").mkdir(exist_ok=True)
(base / "2025-02").mkdir(exist_ok=True)

print(f"Folders created: {list(base.iterdir())}")

for i in range(3):
    log_file = base / "2025-01" / f"server{i+1}.log"
    log_file.write_text(f"Server {i+1} log data")
    print(f"Created: {log_file}")

log_files = glob.glob(str(base / "**/*.log"), recursive=True)
print(f"\nAll log files found: {log_files}")

backup = Path("cloudshield_backup")
backup.mkdir(exist_ok=True)
shutil.copytree(str(base), str(backup / "logs"), dirs_exist_ok=True)
print(f"\nBackup created at: {backup}")

log_path = Path("cloudshield_logs/2025-01/server1.log")

print(f"File name: {log_path.name}")
print(f"Extension: {log_path.suffix}")
print(f"Parent folder: {log_path.parent}")
print(f"File exists: {log_path.exists()}")
print(f"File size: {log_path.stat().st_size} bytes")
print(f"Read content: {log_path.read_text()}")