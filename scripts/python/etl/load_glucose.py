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

glucose_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\glucose.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in glucose_df.iterrows():

    sql = """
    INSERT INTO bronze_glucose (

        user_id,
        glycogen_level,
        measured_at

    )
    VALUES (%s, %s, %s)
    """

    values = (

        int(row["user_id"]),

        float(row["glycogen_level"]),

        row["measured_at"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_glucose loaded successfully")

cursor.close()
conn.close()