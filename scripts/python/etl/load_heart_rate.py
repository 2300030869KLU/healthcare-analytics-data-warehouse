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

heart_rate_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\heart_rate.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in heart_rate_df.iterrows():

    sql = """
    INSERT INTO bronze_heart_rate (

        user_id,
        heart_rate,
        measured_at

    )
    VALUES (%s, %s, %s)
    """

    values = (

        int(row["user_id"]),

        int(row["heart_rate"]),

        row["measured_at"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_heart_rate loaded successfully")

cursor.close()
conn.close()