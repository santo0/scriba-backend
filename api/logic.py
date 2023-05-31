import os
from tempfile import SpooledTemporaryFile
from fastapi import UploadFile

import uuid


class FileManager:
    @classmethod
    async def upload_file(cls, file: UploadFile) -> str:
        raise NotImplementedError()

class LocalFileManager(FileManager):
    STORAGE_PATH = '/home/user/storage/scriba/'
    PROCESSED_PATH = os.path.join(STORAGE_PATH, 'processed/') 
    TO_PROCESS_PATH = os.path.join(STORAGE_PATH, 'to_process/')

    @classmethod
    async def upload_file(cls, file: UploadFile) -> str:
        extension = file.filename.split('.')[-1]
        filename = f'{str(uuid.uuid4().hex)}.{extension}'
        filepath = os.path.join(cls.TO_PROCESS_PATH, filename)
        contents = file.file.read()
        with open(filepath, 'wb') as f:
            f.write(contents)
        return filepath