import pandas as pd
from db_connection import get_connection

# -----------------------------------
# MYSQL CONNECTION
# -----------------------------------

conn = get_connection()

cursor = conn.cursor()

# -----------------------------------
# LOAD CSV
# -----------------------------------

bp_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\bp.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in bp_df.iterrows():

    sql = """
    INSERT INTO bronze_bp (
        bp_id,
        user_id,
        systolic,
        diastolic,
        pulse,
        measured_at,
        notes
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row["bp_id"]),
        int(row["user_id"]),
        int(row["systolic"]),
        int(row["diastolic"]),
        int(row["pulse"]),
        row["measured_at"],
        row["notes"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_bp loaded successfully")

cursor.close()
conn.close()