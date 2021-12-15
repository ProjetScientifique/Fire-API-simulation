from typing import List, Optional
from pydantic import BaseModel

class IncendieBase(BaseModel):
    incendie_latitude: float
    incendie_longitude: float
    incendie_intensite: float

class IncendieCreate(IncendieBase):
    pass

class Incendie(IncendieBase):
    id_incendie: int
    class Config:
        orm_mode = True


class CapteurBase(BaseModel):
    capteur_latitude: float
    capteur_longitude: float
    name_capteur: str

class CapteurCreate(CapteurBase):
    pass

class Capteur(CapteurBase):
    id_capteur: int
    class Config:
        orm_mode = True












class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
    class Config:
        orm_mode = True