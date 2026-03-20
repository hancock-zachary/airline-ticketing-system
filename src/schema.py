#%%
from pydantic import BaseModel


#%%
class Airport(BaseModel):
    code: str = ""
    year: str = ""
    city: str = ""
    country: str = ""

class Aircraft(BaseModel):
    aircraft_id: str = ""
    aircraft_type: str = ""
    capacity: int


#%%
if __name__ == "__main__":
    pass