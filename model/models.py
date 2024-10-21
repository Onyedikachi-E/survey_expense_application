from pydantic import BaseModel
from typing import List, Optional

class Expense(BaseModel):
    utilities: float
    entertainment: float
    school_fees : float
    shopping : float
    healthcare : float


class UserModel(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str
    total_income: float
    expenses: Expense


class UserModelCreate(UserModel):
    user_id: int


class UserModelUpdate(UserModel):
    pass
