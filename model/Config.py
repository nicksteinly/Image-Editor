import os
from dotenv import load_dotenv

load_dotenv('env/.env')
UPLOAD_FILE_PATH = os.getenv('UPLOAD_FILE_PATH', default='../view/public/uploads/')