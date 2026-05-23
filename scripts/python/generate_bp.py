from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

fake = Faker('en_IN')

# -----------------------------------
# LOAD USERS DATA
# -----------------------------------

users_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\users.csv"
)

# -----------------------------------
# CONFIGURATION
# -----------------------------------

START_DATE = datetime(2025, 1, 1)

# -----------------------------------
# GENERATE BP DATA
# -----------------------------------

bp_records = []

bp_id = 1

for _, patient in users_df.iterrows():

    num_readings = random.randint(8, 15)

    for _ in range(num_readings):

        random_days = random.randint(0, 364)

        random_date = START_DATE + timedelta(days=random_days)

        random_hour = random.randint(0, 23)

        random_minute = random.randint(0, 59)

        measured_at = random_date.replace(
            hour=random_hour,
            minute=random_minute
        )

        age = patient["age"]

        # realistic BP ranges
        if age > 60:
            systolic = random.randint(120, 170)
            diastolic = random.randint(80, 110)
        else:
            systolic = random.randint(100, 140)
            diastolic = random.randint(70, 95)

        pulse = random.randint(60, 110)

        bp_records.append({
            "bp_id": bp_id,
            "user_id": patient["user_id"],
            "systolic": systolic,
            "diastolic": diastolic,
            "pulse": pulse,
            "measured_at": measured_at,
            "notes": fake.sentence(nb_words=4)
        })

        bp_id += 1

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

bp_df = pd.DataFrame(bp_records)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

bp_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\bp.csv",
    index=False
)

print("bp.csv generated successfully")