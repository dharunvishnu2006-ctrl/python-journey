from datetime import datetime, timedelta

appointment = "2026-05-23"
dt = datetime.strptime(appointment, "%Y-%m-%d")
next_visit = dt + timedelta(days=30)
print("Next Visit:", next_visit)