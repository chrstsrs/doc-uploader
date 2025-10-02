from fastapi import FastAPI, UploadFile, Form
from producer import publish_event
from db import init_db, insert_upload
import uuid, time, os

app = FastAPI()


@app.on_event("startup")
async def startup():
    init_db()


@app.post("/upload")
async def upload_file(file: UploadFile, user_id: str = Form(...)):
    file_id = str(uuid.uuid4())
    path = f"/data/{file_id}_{file.filename}"
    os.makedirs("/data", exist_ok=True)
    with open(path, "wb") as f:
        f.write(await file.read())
    timestamp = int(time.time())

    insert_upload(file_id, user_id, path, timestamp)

    event = {
        "id": file_id,
        "userId": user_id,
        "path": path,
        "timestamp": timestamp,
    }
    publish_event("image.uploaded", event)
    return {"status": "uploaded", "id": file_id}
