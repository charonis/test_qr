from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse


app = FastAPI(title="qrtest")


@app.get("/get_image")
async def get_image():
    return FileResponse("storage/test.jpg")



@app.post("/post_image")
async def post_image(file: UploadFile ):
    return {"filename": file.filename}
    