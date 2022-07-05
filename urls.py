import os
from dotenv import load_dotenv

load_dotenv()

FRONTEND_BASE_URL = os.getenv('FRONTEND_BASE_URL')
