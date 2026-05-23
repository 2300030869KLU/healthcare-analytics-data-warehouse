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

        user_id,
        oxygen_level,
        measured_at

    )
    VALUES (%s, %s, %s)
    """

    values = (

        int(row["user_id"]),

        float(row["oxygen_level"]),

        row["measured_at"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_oxygen loaded successfully")

cursor.close()
conn.close()