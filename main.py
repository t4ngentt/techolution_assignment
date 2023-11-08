import random
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import uvicorn
import aiofiles
import techolution
import os
from pathlib import Path

resumepath = Path() / 'resumes'

app = FastAPI()


@app.post('/deletefiles/')
async def deletefiles():
    try:
        files = os.listdir(resumepath)
        for file in files:
            file_path = os.path.join(resumepath, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        return {"All files deleted successfully."}
    except OSError:
        return {"Error occurred while deleting files."}

    # return {"filenames": [f.filename for f in file_uploads]}

@app.post('/uploadfile/')
async def create_upload_file(file_uploads: list[UploadFile]): 
    for file_upload in file_uploads:
        data = await file_upload.read()
        save_to = resumepath / file_upload.filename
        with open(save_to, 'wb') as f:
            f.write(data)

    return {"filenames": [f.filename for f in file_uploads]}


@app.get("/initiatequery")
async def initiatequery(job_desc : str):
    dicstring = techolution.initiate(job_desc)  
    # return {'response' : dicstring}
    return JSONResponse(content=jsonable_encoder(dicstring))

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    print("running")

