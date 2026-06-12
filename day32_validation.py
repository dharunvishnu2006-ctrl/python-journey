from pydantic import BaseModel, ValidationError, Field
from typing import Optional

class ThreatReport(BaseModel):
    ip_address: str
    severity: str = Field(pattern="^(LOW|MEDIUM|HIGH)$")
    request_count: int = Field(ge=0)
    description: Optional[str] = None

try:
    report1 = ThreatReport(
        ip_address="192.168.1.1",
        severity="HIGH",
        request_count=1500
    )    
    print("Valid report:", report1)
except Exception as e:
    print("Error:", e)

try:
    report2 = ThreatReport(
        ip_address="10.0.0.1",
        severity="CRITICAL",
        request_count=200
    )        
    print("Valid report:", report2)
except Exception as e:
    print("Error:", e)    

import pandas as pd
from pydantic import BaseModel, ValidationError

class LogEntry(BaseModel):
    ip_address: str
    status: str
    requests: int = Field(ge=0)

data = {
    'ip_address': ['192.168.1.1', '10.0.0.1', 'invalid_ip', '172.16.0.1'],
    'status': ['suspicious', 'normal', 'suspicious', 'normal'],
    'requests': [1500, 200, -50, 300]  # -50 invalid!
}

df = pd.DataFrame(data)

valid_rows = []
invalid_rows = []

for index, row in df.iterrows():
    try:
        entry = LogEntry(
            ip_address=row['ip_address'],
            status=row['status'],
            requests=row['requests']
        )
        valid_rows.append(entry)
    except ValidationError as e:
        invalid_rows.append((index, str(e)))

print(f"Valid rows: {len(valid_rows)}")
print(f"Invalid rows: {len(invalid_rows)}")
for idx, error in invalid_rows:
    print(f"Row {idx} error: {error[:100]}...")