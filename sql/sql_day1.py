import pandas as pd
import mysql.connector
import numpy as np

# 1️⃣ Load CSV and select all 12 columns
df = pd.read_csv(
    r'C:\Users\HP\Documents\Python\sql\titanic.csv',
    usecols=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex',
             'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
)

# 2️⃣ Replace all NaN (numeric or object) with Python None
df = df.replace({np.nan: None})

# 3️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="gilmoregirl01Z"
)
cursor = conn.cursor()

# 4️⃣ Create database and table
cursor.execute("CREATE DATABASE IF NOT EXISTS practice;")
cursor.execute("USE practice;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS titanic_full (
    PassengerId INT,
    Survived INT,
    Pclass INT,
    Name VARCHAR(100),
    Sex VARCHAR(10),
    Age FLOAT,
    SibSp INT,
    Parch INT,
    Ticket VARCHAR(50),
    Fare FLOAT,
    Cabin VARCHAR(50),
    Embarked VARCHAR(10)
);
""")

# 5️⃣ Insert rows safely
for row in df.itertuples(index=False, name=None):
    cursor.execute("""
        INSERT INTO titanic_full 
        (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, row)

# 6️⃣ Commit and close
conn.commit()
cursor.close()
conn.close()

print("CSV imported successfully!")

