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
# GENERATE TEMPERATURE DATA
# -----------------------------------

temperature_records = []

temp_id = 1

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

        month = measured_at.month

        # seasonal temperature variation
        if month in [4, 5, 6]:
            temperature = round(random.uniform(98.6, 102.5), 1)
        else:
            temperature = round(random.uniform(97.0, 100.0), 1)

        temperature_records.append({
            "temp_id": temp_id,
            "user_id": patient["user_id"],
            "temperature_value": temperature,
            "measured_at": measured_at,
            "notes": fake.sentence(nb_words=4),
            "unit": "F"
        })

        temp_id += 1

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

temperature_df = pd.DataFrame(temperature_records)

# -----------------------------------
# EXPORT CSV
# -----------------------------------

temperature_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\temperature.csv",
    index=False
)

print("temperature.csv generated successfully")