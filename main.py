from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import GenerateInput

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_methods=['*'],
    allow_headers=['*']
)


@app.post("/v1/api/generate/ganjil")
def ganjil(data: GenerateInput):
    numbers = [i for i in range(data.angka+1) if i % 2 != 0]
    return {"result": numbers}

@app.post("/v1/api/generate/prisma")
def prisma(data: GenerateInput):
    bil_prisma = []
    index = 1
    while True:
        new_bil_prisma = (index * (index+1) * (index+2)) // 6
        if new_bil_prisma > data.angka:
            break
        data.angka
        bil_prisma.append(new_bil_prisma)
        index += 1


    return {"result": bil_prisma}