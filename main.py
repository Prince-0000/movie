# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from routes.recommendations import route as route1
#
#
#
# app=FastAPI()
#
#
# #add
#
# origins =[
#     "http://localhost",
#     "http://localhost:3000",
#     "*"
# ]
#
# @app.get('/')
# def test():
#     return 'route is working fine'
# app.include_router(route1,tags=['recommend'])
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"]
#
# )
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)