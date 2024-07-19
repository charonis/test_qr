from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
import os
from createQr import qr


app = FastAPI(title="qrtest")


@app.get("/get_image")
async def get_image(index: int):
    try:
        content = os.listdir("storage")
        return FileResponse(f"storage/{content[index]}")
    except: 
        return {"error: not find index"}


@app.get("/get_all_image")
async def get_all_image():
    content = os.listdir("storage")
    return content


@app.post("/post_image")
async def post_image(file: UploadFile ):
    content = file.file.read()
    with open(file=f"storage/{file.filename}", mode="wb", ) as image:
        image.write(content )
    return {"filename": file.filename}

@app.post("/create_qr")
async def create_qr(name: str, first_name: str, pathonimy: str):
    return qr(name, first_name, pathonimy)


@app.post("/post_add_file")
async def post_add_file():
    return f"{os.listdir(".")} - f{os.listdir("storage")}"
    

# print(qr("haha", "hsdlf", "lsfdjls"))