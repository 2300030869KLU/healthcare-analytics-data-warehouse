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

oxygen_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\oxygen.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in oxygen_df.iterrows():

    sql = """
    INSERT INTO bronze_oxygen (
        oxygen_id,
        user_id,
        oxygen_level,
        measured_at,
        notes,
        unit
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row["oxygen_id"]),
        int(row["user_id"]),
        float(row["oxygen_level"]),
        row["measured_at"],
        row["notes"],
        row["unit"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_oxygen loaded successfully")

cursor.close()
conn.close()