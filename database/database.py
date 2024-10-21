from pymongo import MongoClient

# Set up an instance of the MongoClient()
client = MongoClient(host="localhost", port=27017)

# Initialize the database
db = client.survey_manager

# Create the the Collection
user_collection = db.user_demography




