import pandas as pd
import random

# -----------------------------------
# LOAD HEALTH SESSIONS
# -----------------------------------

sessions_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\health_sessions.csv"
)

# -----------------------------------
# GENERATE BP DATA
# -----------------------------------

bp_records = []

for _, row in sessions_df.iterrows():

    systolic = random.randint(100, 180)

    diastolic = random.randint(60, 120)

    bp_records.append({

        "user_id": row["user_id"],

        "systolic": systolic,

        "diastolic": diastolic,

        "measured_at": row["measured_at"]
    })

# -----------------------------------
# CREATE DATAFRAME
# -----------------------------------

bp_df = pd.DataFrame(
    bp_records
)

# -----------------------------------
# SAVE CSV
# -----------------------------------

bp_df.to_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\bp.csv",
    index=False
)

print("bp.csv generated successfully")