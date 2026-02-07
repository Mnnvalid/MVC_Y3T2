from models.database import get_db
from datetime import date

class Citizen:
    @staticmethod
    def get_all():
        db = get_db()
        return db.execute("SELECT * FROM citizens").fetchall()
    
    @staticmethod
    def create(data):
        db = get_db()
        exists = db.execute(
            "SELECT * FROM citizens WHERE national_id = ?",
            (data['national_id'],)
        ).fetchone()
        if exists:
            return False
        
        db.execute (
            "INSERT INTO citizens VALUES (NULL,?,?,?,?,?)",
            (
                data['national_id'],
                data['age'],
                data['health_risk'],
                date.today(),
                data['citizen_type']
            )
        )
        db.commit()
        return True
    