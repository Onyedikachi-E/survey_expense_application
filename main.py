from flask import abort
from flask import Flask
from flask import request
from flask import jsonify
from http import HTTPStatus
from markupsafe import escape
from flask import render_template
from repository.user_repo import User
from database.database import user_collection
from werkzeug.exceptions import HTTPException
from model.models import UserModelCreate, UserModelUpdate


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/user", methods=["POST"])
def create_user():
    """
    This route handles the creation of users
    """
    try:
        # Extract user_data from the request JSON body
        user_data = request.get_json()
        print(user_data)

        user_data = {
            "first_name": "Chinasa",
            "last_name": "Okeke",
            "age": 34,
            "gender": "Female",
            "user_id": 2,
            "total_income": 40000,
            "expense": {
                "utilities": 30,
                "entertainment": 50,
                "school_fees": 60,
                "shopping": 70,
                "healthcare": 40
            }
        }
        print(user_data)
        
        if not user_data:
            return jsonify({"message": "User information was not supplied"}), HTTPStatus.BAD_REQUEST

        # Initiate the User instance
        user_repo = User(user_collection=user_collection)
        
        # Create the user with the provided data
        print(user_collection)
        user_repo.create_user_data(user_data=user_data)
        return jsonify(message="User created successfully"), HTTPStatus.CREATED
    
    except Exception as err:
        raise HTTPException(description=f"Database error: {str(err)}", response=HTTPStatus.BAD_REQUEST)


@app.route("/api/user/all", methods=["GET"])
def fetch_all_user():
    """
    This routes retrieves all users data
    """
    try:
        # Initiate the user instance
        user_repo = User(user_collection=user_collection)

        # Fetch all the records from the database
        all_users = user_repo.fetch_all_user()
        users_list = list(all_users)

        for user in users_list:
            user['_id'] = str(user['_id'])

        return jsonify(users_list)

    except Exception as err:
        abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")


@app.route("/api/user/one/<user_id>", methods=["GET"])
def fetch_one_user(user_id):
    """
    This routes retrieves one user data
    """
    try:
        # Intitiate the user instance
        user_repo = User(user_collection=user_collection)

        # Fetch one user records from the database
        user = user_repo.fetch_one_user(user_id=user_id)
        user['_id'] = str(user['_id'])
        return jsonify(user)

    except Exception as err:
        abort(code=HTTPStatus.BAD_REQUEST, description=f"Database error: {str(err)}")


@app.route("/api/user/one/<user_id>", methods=["PUT"])
def update_user(user_id):
    """
    This routes updates the user usin the update data
    """

    try:
        # Extract user_data from the request JSON body
        user_update_data:UserModelUpdate=request.get_json(force=True)

        if not user_update_data:
            return jsonify({"message": "User information was not supplied"}), HTTPStatus.BAD_REQUEST

        # Initiate the User instance
        user_repo = User(user_collection=user_collection)

        # Update the user with the provided data
        user_repo.update_user_data(user_id=user_id, update_data=user_update_data)
        return jsonify(message="User Updated successfully"), HTTPStatus.PARTIAL_CONTENT
    
    except Exception as err:
        raise HTTPException(description=f"Database error: {str(err)}", response=HTTPStatus.BAD_REQUEST)
    

@app.route("/api/user/one/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    """
    This route deletes the use document from the database
    """

    try:
        # Initiate the user instance
        user_repo = User(user_collection=user_collection)

        # Delete the record from the database
        user_repo.delete_user_data(user_id=user_id)
        return jsonify(message="User Deleted successfully"), HTTPStatus.OK

    except Exception as err:
        raise HTTPException(description=f"Database error: {str(err)}", response=HTTPStatus.BAD_REQUEST)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=True)