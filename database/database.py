from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Connection string to MongoDB Atlas
uri = "mongodb+srv://admin:admin123@servermanager.j0y1z.mongodb.net/survey_manager?retryWrites=true&w=majority&appName=servermanager"

# Set up an instance of the MongoClient()
client = MongoClient(uri, server_api=ServerApi('1'))

# Initialize the database
db = client.survey_manager

# Create the the Collection
user_collection = db.user_demography
