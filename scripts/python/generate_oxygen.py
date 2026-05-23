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
# GENERATE OXYGEN DATA
# -----------------------------------

oxygen_records = []

oxygen_id = 1

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

        # realistic SpO2 ranges
        if age > 60:
            oxygen_level = random.randint(88, 100)
        else:
            oxygen_level = random.randint(92, 100)

        oxygen_records.append({
            "oxygen_id": oxygen_id,
            "user_id": patient["user_id"],
            "oxygen_level": oxygen_level,
            "measured_at": measured_at,
            "notes": fake.sentence(nb_words=4),
            "unit": "%"
        })

        oxygen_id += 1

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

oxygen_df = pd.DataFrame(oxygen_records)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

oxygen_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\oxygen.csv",
    index=False
)

print("oxygen.csv generated successfully")