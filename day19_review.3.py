from datetime import datetime, timedelta
import re

appointments = [
    "Patient: P001, Date: 2026-05-23, Phone: 9876543210",
    "Patient: P002, Date: 2026-06-15, Phone: 8765432109",
    "Patient: P003, Date: 2026-07-01, Phone: 7654321098"
]

for appointment in appointments:
    phone = re.search(r'\d{10}', appointment).group()
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', appointment).group()
    appointment_date = datetime.strptime(date_match, "%Y-%m-%d")
    next_appointment = appointment_date + timedelta(days=30)

    print("Phone:", phone)
    print("Current Appointment:", appointment_date.strftime("%d/%m/%Y"))
    print("Next Appointment:", next_appointment.strftime("%d/%m/%Y"))
    print("-" * 40)