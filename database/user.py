import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
user_app = firebase_admin.initialize_app(cred, name="user_db")
db = firestore.client(user_app)

class UserDatabase:

    def __init__(self):
        self.user_db = db.collection("user")

    def getAllUsers(self):
        """
        Retrieve all users
        """
        users = [user.to_dict() for user in self.user_db.stream()]
        return users
    
    def getUsersByRole(self, role_id):
        """
        Retrieve Users by Role, if record does not exist, raise Assertion Error
        """
        users = self.user_db.where(filter=FieldFilter("role", "==", int(role_id))).stream()
        users_list = [user.to_dict() for user in users]
        if users_list == []:
            raise AssertionError
        else:
            return users_list
    
    def getUserByUsername(self, username):
        """
        Retrieve User by Username, if record does not exist, raise Assertion Error
        """
        if self.user_db.document(username).get().to_dict() is None:
            raise AssertionError
        else:
            user = self.user_db.document(username).get().to_dict()
            return user
    
    def getUserByEmail(self, email):
        """
        Retrieve User by Email, if record does not exist, raise Assertion Error
        """
        users = self.user_db.where(filter=FieldFilter("email", "==", email)).stream()
        users_list = [user.to_dict() for user in users]
        if users_list == [] and len(users_list) > 1:
            raise AssertionError
        else:
            return users_list[0]

    def addUser(self, username, user_json):
        """
        Add User into Database, if record already exists, raise Assertin Error
        """
        if self.user_db.document(username).get().to_dict() is not None:
            raise AssertionError
        else:
            self.user_db.document(username).set(user_json)

    def updateUser(self, old_username, new_username, user_json):
        """
        Update User in Database, if record not found in database, raise Assertion Error
        """
        if self.user_db.document(old_username).get().to_dict() is None:
            raise AssertionError
        else:
            self.user_db.document(old_username).delete()
            user_json["oldUsername"] = user_json["username"]
            self.user_db.document(new_username).set(user_json)

    def deleteUser(self, username):
        """
        Delete User from database. If it does not exist, raise Assertion Error
        """
        if self.user_db.document(username).get().to_dict() is None:
            raise AssertionError
        else:
            self.user_db.document(username).delete()