from models.database import get_db

db = get_db()
cur = db.cursor()

cur.execute("""
CREATE TABLE shelters (
            shelter_id INTEGER PRIMARY KEY AUTOINCREMENT,
            capacity INTEGER,
            risk_level TEXT
            )
""")

cur.execute("""
CREATE TABLE citizens (
            citizen_id INTEGER PRIMARY KEY AUTOINCREMENT,
            national_id TEXT UNIQUE,
            age INTEGER,
            health_risk INTEGER,
            register_date TEXT,
            citizen_type TEXT
            )
""")

cur.execute("""
CREATE TABLE assignments (
            assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            shelter_id INTEGER,
            citizen_id INTEGER,
            assignment_date TEXT,
            )
""")

shelter = [
    (10,"LOW"),(5,"HIGH"),(8,"LOW"),(4,"MEDIUM"),(6,"LOW")
]

citizens = []
for i in range(1,31):
    if i % 10 == 0:
        ctype = "VIP"
    elif i % 5 == 0:
        ctype = "RISK"
    else:
        ctype = "GENERAL"
    citizens.append((
        None,
        f"11017000000{i:02d}",
        8 + (i % 70),
        1 if i % 4 == 0 else 0,
        "2026-02-01",
        ctype
    )
)

cur.executemany("INSERT INTO shelters VALUES (NULL,?,?)", shelters)
cur.executemany("INSERT INTO citizens VALUES (NULL,?,?,?,?,?)", citizens)

db.commit()
db.close()