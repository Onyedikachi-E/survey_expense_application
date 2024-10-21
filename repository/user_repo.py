from flask import abort
from http import HTTPStatus
from pymongo.errors import PyMongoError
from pymongo.collection import Collection
from werkzeug.exceptions import HTTPException
from model.models import UserModelCreate, UserModelUpdate


# Create a User Class with CRUD Methods
class User():
    def __init__(self, user_collection:Collection):
        self.user_collection = user_collection

    
    def create_user_data(self, user_data:UserModelCreate):
        "Create user information in the database"
        try:

            # Create a document for the user
            print(user_data)
            new_user = self.user_collection.insert_one(document=user_data)
            print("We are good")
            return new_user

        except Exception as err:
            raise HTTPException(description=f"Database error: {str(err)}", response=HTTPStatus.BAD_REQUEST)


    def fetch_all_user(self):
        """'
        Fetch all the user information from the database
        """
        try:

            # Fetch all from all the documents
            all_users = self.user_collection.find({})
            return all_users

        except PyMongoError as err:
            abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")


    def fetch_one_user(self, user_id:int):
        """
        Fetch user information for a user from the database
        """
        try:

            # Cast the user_id parameter to integer
            user_id=int(user_id)

            # Fetch the user document by user_id
            user = self.user_collection.find_one(filter={"user_id":user_id})
            
            # Check if user exists in the database
            if user:
                return user
            else:
                abort(code=HTTPStatus.NOT_FOUND, description=f"User with ID {user_id} not found.")

        except PyMongoError as err:
            abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")


    def update_user_data(self, user_id: int, update_data: UserModelUpdate):
        """
        Update the record of a user using the update data.
        """
        try:
            # Cast the user_id parameter to integer
            user_id = int(user_id)

            # Check if user exists in the database
            user_exist = self.fetch_one_user(user_id=user_id)
            if user_exist:
        
                self.user_collection.update_one(filter={"user_id": user_id}, update={"$set": update_data})
                return {"message": "User record has been updated successfully"}

            else:
                abort(code=HTTPStatus.NOT_FOUND, description=f"User with ID {user_id} not found.")

        except PyMongoError as err:
            abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")


    def delete_user_data(self, user_id: int):
        """
        Delete the record of a user from the database
        """
        try:
            # Cast the user_id parameter to integer
            user_id = int(user_id)

            # Check if user exists in the database
            user_exist = self.fetch_one_user(user_id=user_id)
            if user_exist:

                self.user_collection.delete_one(filter={"user_id":user_id})
                return {"message": "User record has been deleted successfully"}
            
            else:
                abort(code=HTTPStatus.NOT_FOUND, description=f"User with ID {user_id} not found.")
            
        except PyMongoError as err:
            abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")







