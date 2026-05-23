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

temperature_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\temperature.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in temperature_df.iterrows():

    sql = """
    INSERT INTO bronze_temperature (
        temp_id,
        user_id,
        temperature_value,
        measured_at,
        notes,
        unit
    )
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row["temp_id"]),
        int(row["user_id"]),
        float(row["temperature_value"]),
        row["measured_at"],
        row["notes"],
        row["unit"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_temperature loaded successfully")

cursor.close()
conn.close()