from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker('en_IN')

# -----------------------------------
# CONFIGURATION
# -----------------------------------

NUM_PATIENTS = 5000

START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

# Andhra Pradesh & Telangana Cities
LOCATIONS = [
    ("Vijayawada", "Andhra Pradesh"),
    ("Visakhapatnam", "Andhra Pradesh"),
    ("Guntur", "Andhra Pradesh"),
    ("Tirupati", "Andhra Pradesh"),
    ("Kurnool", "Andhra Pradesh"),
    ("Ongole", "Andhra Pradesh"),
    ("Ponnur", "Andhra Pradesh"),

    ("Hyderabad", "Telangana"),
    ("Warangal", "Telangana"),
    ("Karimnagar", "Telangana"),
    ("Nizamabad", "Telangana"),
    ("Khammam", "Telangana")
]

GENDERS = ["Male", "Female"]

# -----------------------------------
# AGE GROUP FUNCTION
# -----------------------------------

def get_age_group(age):
    if age <= 18:
        return "0-18"
    elif age <= 30:
        return "19-30"
    elif age <= 45:
        return "31-45"
    elif age <= 60:
        return "46-60"
    else:
        return "60+"

# -----------------------------------
# GENERATE PATIENTS
# -----------------------------------

patients = []

for patient_id in range(1, NUM_PATIENTS + 1):

    name = fake.name()

    age = random.randint(10, 85)

    gender = random.choice(GENDERS)

    city, state = random.choice(LOCATIONS)

    dob = datetime.now() - timedelta(days=age * 365)

    patients.append({
        "user_id": patient_id,
        "username": name,
        "email": fake.email(),
        "date_of_birth": dob.date(),
        "location": city,
        "state": state,
        "gender": gender,
        "age": age,
        "age_group": get_age_group(age)
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

patients_df = pd.DataFrame(patients)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

patients_df.to_csv(r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\users.csv", index=False)

print("users.csv generated successfully")