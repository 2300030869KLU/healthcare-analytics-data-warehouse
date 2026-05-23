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

users_df = pd.read_csv(
    r"C:\HEATHCARE_WAREHOUSE\healthcare-analytics-data-warehouse\datasets\users.csv"
)

# -----------------------------------
# INSERT DATA
# -----------------------------------

for _, row in users_df.iterrows():

    sql = """
    INSERT INTO bronze_users (
        user_id,
        username,
        email,
        date_of_birth,
        location,
        state,
        gender,
        age,
        age_group
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row["user_id"]),
        row["username"],
        row["email"],
        row["date_of_birth"],
        row["location"],
        row["state"],
        row["gender"],
        int(row["age"]),
        row["age_group"]
    )

    cursor.execute(sql, values)

# -----------------------------------
# COMMIT
# -----------------------------------

conn.commit()

print("bronze_users loaded successfully")

cursor.close()
conn.close()