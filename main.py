import DataHandler
import model_morador

from fastapi import FastAPI

print("Starting FastAPI application...")

dt_handler = DataHandler.DataHandler("PREDIO.db")

app = FastAPI()


@app.get("/morador/{morador_id}")
async def get_morador(morador_id: str):
    morador = await dt_handler.get_morador(morador_id)
    if morador is None:
        return {"message": "Morador não encontrado"}
    return {"message": "dados morador", "morador": morador.__dict__}

@app.get("/moradores/")
async def get_moradores():
    moradores = await dt_handler.get_moradores()
    return {"message": "Lista de moradores", "moradores": [morador.__dict__ for morador in moradores]}

@app.post("/morador/")
async def create_morador(nome: str, bloco: str, ap: int, senha: str):
    morador = model_morador.Morador(nome, bloco, ap, senha)
    await dt_handler.insert_morador(morador)
    return {"message": "Morador cadastrado com sucesso", "morador": morador.__dict__}