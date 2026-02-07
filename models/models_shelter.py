from models.database import get_db

class Shelter:
    @staticmethod
    def get_all():
        return get_db().execute("SELECT * FROM shelters").fetchall()
    
    @staticmethod
    def current_count(shelter_id):
        return get_db().execute(
            "SELECT COUNT(*) FROM assignments WHERE shelter_id = ?", (shelter_id,)
        ).fetchone()[0]