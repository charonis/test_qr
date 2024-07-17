from fastapi import FastAPI
from fastapi.responses import FileResponse


app = FastAPI(title="qrtest")


@app.get("/get_image")
async def get_image():
    return FileResponse("storage/test.jpg")



