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
# GENERATE HEART RATE DATA
# -----------------------------------

heart_rate_records = []

hr_id = 1

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

        # realistic heart rate ranges
        if age > 60:
            heart_rate = random.randint(60, 110)
        else:
            heart_rate = random.randint(55, 100)

        heart_rate_records.append({
            "hr_id": hr_id,
            "user_id": patient["user_id"],
            "heart_rate": heart_rate,
            "measured_at": measured_at,
            "notes": fake.sentence(nb_words=4),
            "unit": "bpm"
        })

        hr_id += 1

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

heart_rate_df = pd.DataFrame(heart_rate_records)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

heart_rate_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\heart_rate.csv",
    index=False
)

print("heart_rate.csv generated successfully")