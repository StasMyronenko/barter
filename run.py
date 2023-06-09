from fastapi import FastAPI


def run_fastapi_server():
    app = FastAPI()

    @app.get("/")
    async def root():
        return {"message": "Hello World"}