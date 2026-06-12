from datetime import datetime, date, timedelta

now = datetime.now()
print("Current DateTime:", now)

print("Formatted:", now.strftime("%d/%m/%Y %H:%M"))

tomorrow = now + timedelta(days=1)
print("Tomorrow:", tomorrow.strftime("%d/%m/%Y"))

appointment = now + timedelta(days=7)
print("Next Appointment:", appointment.strftime("%d/%m/%Y"))

birthday = date(2006, 5, 21)
today = date.today()
age_days = today - birthday
print(f"Dharun's age in days: {age_days.days} days!")