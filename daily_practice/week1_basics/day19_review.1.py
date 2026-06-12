from datetime import datetime, timedelta

now = datetime.now()

current_date = now.strftime("%d/%m/%Y")
print("Current Date:", current_date)

next_checkup = now + timedelta(days=30)
print("AAROGYA Next Checkup:", next_checkup.strftime("%d/%m/%Y"))