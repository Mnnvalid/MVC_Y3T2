from models.database import get_db
from datetime import date

class Assignment:
    @staticmethod
    def assign(citizen):
        db = get_db()
        
        if citizen[3] == 1:
            shelters = db.execute(
                "SELECT * FROM shelters WHERE risk_level = 'LOW'"
            ).fetchall()
        else:
            shelters = db.execute("SELECT * FROM shelters").fetchall()
        
        for s in shelters:
            count = db.execute(
                "SELECT COUNT(*) FROM assignments WHERE shelter_id = ?", (s[0],)
            ).fetchone()[0]

            if count < s[1]:
                db.execute(
                    "INSERT INTO assignments VALUES (NULL,?,?,?)",
                    (s[0], citizen[0], date.today())
                )
                db.commit()
                return True
        
        return False