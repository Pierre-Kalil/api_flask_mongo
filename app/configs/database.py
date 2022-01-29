from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

DATABASE = os.environ.get('DATABASE')

client = MongoClient()

db = client[DATABASE]