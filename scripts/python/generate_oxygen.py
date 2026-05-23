import pandas as pd
import random

# -----------------------------------
# LOAD HEALTH SESSIONS
# -----------------------------------

sessions_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv"
)

# -----------------------------------
# GENERATE OXYGEN DATA
# -----------------------------------

oxygen_records = []

for _, row in sessions_df.iterrows():

    oxygen_records.append({

        "user_id": row["user_id"],

        "oxygen_level": random.randint(90, 100),

        "measured_at": row["measured_at"]
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

oxygen_df = pd.DataFrame(
    oxygen_records
)

# -----------------------------------
# SAVE CSV
# -----------------------------------

oxygen_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\oxygen.csv",
    index=False
)

print("oxygen.csv generated successfully")