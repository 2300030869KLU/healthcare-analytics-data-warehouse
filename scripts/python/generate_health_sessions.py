import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------------
# LOAD USERS
# -----------------------------------

users_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\users.csv"
)

# -----------------------------------
# GENERATE HEALTHCARE SESSIONS
# -----------------------------------

sessions = []

START_DATE = datetime(2025, 1, 1)

for _, row in users_df.iterrows():

    user_id = row["user_id"]

    # number of healthcare activity days
    total_sessions = random.randint(30, 80)

    for _ in range(total_sessions):

        random_days = random.randint(0, 364)

        session_date = START_DATE + timedelta(
            days=random_days
        )

        session_time = timedelta(
            hours=random.randint(6, 22),
            minutes=random.randint(0, 59)
        )

        measured_at = session_date + session_time

        sessions.append({

            "user_id": user_id,

            "measured_at": measured_at
        })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

sessions_df = pd.DataFrame(sessions)

# -----------------------------------
# SAVE CSV
# -----------------------------------

sessions_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv",
    index=False
)

print("health_sessions.csv generated successfully")