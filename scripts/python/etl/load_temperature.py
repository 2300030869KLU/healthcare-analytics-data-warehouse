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

        user_id,
        temperature_value,
        measured_at

    )
    VALUES (%s, %s, %s)
    """

    values = (

        int(row["user_id"]),

        float(row["temperature_value"]),

        row["measured_at"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_temperature loaded successfully")

cursor.close()
conn.close()