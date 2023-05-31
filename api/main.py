import os
from fastapi import FastAPI, HTTPException,File, UploadFile
from pydantic import BaseModel
from typing import List, Optional
import json
from logic import LocalFileManager
app = FastAPI()



@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        filepath = await LocalFileManager.upload_file(file)
        # send filepath to queue
    except Exception as e:
        print(e)
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename} --- {filepath}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
