import numpy as np

bp = np.array([120,145,118,160,135,155,112,170])

high_risk = bp[bp > 140]
normal_patient_count = np.sum( bp <= 140)
high_risk_patient = np.sum (bp > 140)

mean_bp = np.mean(bp)

print("High Risk BP:", high_risk)
print("Normal Count:", normal_patient_count)
print("High Risk Count:", high_risk_patient)
print("Mean BP:", mean_bp)