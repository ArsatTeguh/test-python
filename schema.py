from pydantic import BaseModel, validator
from fastapi import HTTPException

class GenerateInput(BaseModel):
    angka: int

    @validator("angka")
    def angka_must_not_empty(cls, value):
        if value <= 0:
            raise HTTPException(
                status_code=400, detail="Inputa tidak boleh kosong atau bernilai dibawah 0"
            )
        return value
