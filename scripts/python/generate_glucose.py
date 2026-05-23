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
# GENERATE GLUCOSE DATA
# -----------------------------------

glucose_records = []

glycogen_id = 1

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

        # realistic glucose ranges
        if age > 60:
            glucose = random.randint(90, 240)
        elif age > 45:
            glucose = random.randint(85, 200)
        else:
            glucose = random.randint(70, 160)

        glucose_records.append({
            "glycogen_id": glycogen_id,
            "user_id": patient["user_id"],
            "glycogen_level": glucose,
            "measured_at": measured_at,
            "notes": fake.sentence(nb_words=4),
            "unit": "mg/dL"
        })

        glycogen_id += 1

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

glucose_df = pd.DataFrame(glucose_records)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

glucose_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\glucose.csv",
    index=False
)

print("glucose.csv generated successfully")