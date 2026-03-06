from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from POS.router import POS_router


app = FastAPI() 

app.add_middleware( 

    CORSMiddleware, 
    allow_origins=["http://localhost:5173,http://localhost:5174"], 
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(
    POS_router, 
    prefix="/POS_router", 
    tags=["POS_router"],
)

@app.get("/") 
def read_root(): 
    return {"Hello": "World"}