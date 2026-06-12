# Sample Data
heart_rate = {
    "P101": 72,
    "P102": 105,
    "P103": 88,
    "P104": 120,
    "P105": 65,
    "P106": 98,
    "P107": 110,
    "P108": 70,
    "P109": 85,
    "P110": 130
}

# 1. Critical patients (heart rate > 100)
critical_patients = []
for patient, rate in heart_rate.items():
    if rate > 100:
        critical_patients.append(patient)

# 2. Highest and lowest heart rate
highest = max(heart_rate, key=heart_rate.get)
lowest = min(heart_rate, key=heart_rate.get)

# 3. Average heart rate
average = sum(heart_rate.values()) / len(heart_rate)

# 4. Count stable patients (60–100 bpm)
stable = 0
for rate in heart_rate.values():
    if 60 <= rate <= 100:
        stable += 1

# Output
print("Critical Patients:")
for patient in critical_patients:
    print(patient)

print(f"\nHighest Heart Rate: {highest} ({heart_rate[highest]} bpm)")
print(f"Lowest Heart Rate: {lowest} ({heart_rate[lowest]} bpm)")
print(f"Average Heart Rate: {average:.1f} bpm")
print("Stable Patients:", stable)