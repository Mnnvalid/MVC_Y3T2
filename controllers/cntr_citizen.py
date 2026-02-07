from models.models_citizen import Citizen

def list_citizens():
    return Citizen.get_all()

