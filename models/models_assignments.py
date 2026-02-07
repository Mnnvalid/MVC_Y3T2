from modes.database import get_db
from datetime import date

class Assignment:
    @staticmethod
    def assign(citizen):
        db = get_db()
        
        if citizen[3] == 1:
            shelter = db.execute(
                "SELECT * FROM shelters WHERE risk_level = 'LOW'"
            ).fetchone()
        else:
            shelter = db.execute("SELECT * FROM shelters").fetchone()
        
        for s in shelter:
            count = db.execute(
                "SELECT COUNT(*) FROM assignments WHERE shelter_id = ?", (s[0],)
            ).fetchone()[0]

            if count < s[2]:
                db.execute(
                    "INSERT INTO assignments VALUES (NULL,?,?,?)",
                    (s[0], citizen[0], date.today())
                )
                db.commit()
                return True
        return False