import DataHandler as DataHandler
import Morador.model_morador as model_morador

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

print("Starting FastAPI application...")

dt_handler = DataHandler.DataHandler("PREDIO.db")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.get("/api/morador/{morador_id}")
async def get_morador(morador_id: str):
    morador = await dt_handler.get_morador(morador_id)
    if morador is None:
        return {"message": "Morador não encontrado"}
    return {"message": "dados morador", "morador": morador.__dict__}


@app.get("/api/moradores/")
async def get_moradores():
    moradores = await dt_handler.get_moradores()
    if not moradores:
        return {"message": "Nenhum morador cadastrado"}
    return {"message": f"Lista de moradores com {len(moradores)} pessoas", "moradores": [morador.__dict__ for morador in moradores]}

@app.post("/api/moradores/{apartamento}/validar")
async def validar_morador(apartamento: str, senha: str):
    acesso = await dt_handler.registro_entrada_senha(apartamento, senha)

    if acesso != None:
        return {"message": "Acesso permitido, registrando entrada", "morador": acesso.__dict__}
    else:
        return {"message": "Acesso negado, senha incorreta ou morador não encontrado"}

@app.post("/api/morador/")
async def create_morador(nome: str, bloco: str, ap: int, senha: str):
    morador = model_morador.Morador(nome, bloco, ap, senha)
    morador.id = await dt_handler.insert_morador(morador)
    return {"message": "Morador cadastrado com sucesso", "morador": morador.__dict__}

@app.put("/api/morador/{morador_id}")
async def update_morador(morador_id: str, nome: str = None, bloco: str = None, ap: int = None, senha: str = None):
    morador = await dt_handler.get_morador(morador_id)
    if morador is None:
        return {"message": "Morador não encontrado"}
    
    if nome is not None:
        morador.nome = nome
    if bloco is not None:
        morador.bloco = bloco
    if ap is not None:
        morador.ap = ap
    if senha is not None:
        morador.senha = senha
    
    morador = await dt_handler.update_morador(morador)
    return {"message": "Morador atualizado com sucesso", "morador": morador.__dict__}

@app.put("/api/morador/{morador_id}/controle")
async def registro_entrada_saida(morador_id: str):
    morador = await dt_handler.get_morador(morador_id)
    if morador is None:
        return {"message": "Morador não encontrado"}
    
    morador = await dt_handler.registro_entrada_saida(morador)
    return {"message": "Registro de entrada/saída atualizado com sucesso", "morador": morador.__dict__}

@app.delete("/api/morador/{morador_id}")
async def delete_morador(morador_id: str):
    morador = await dt_handler.get_morador(morador_id)
    if morador is None:
        return {"message": "Morador não encontrado"}
    
    await dt_handler.delete_morador(morador.id)
    return {"message": "Morador deletado com sucesso"}