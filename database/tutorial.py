import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import json

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
tutorial_app = firebase_admin.initialize_app(cred, name="tutorial_db")
db = firestore.client(tutorial_app)

class TutorialDatabase:

    def __init__(self):
        self.tutorial_db = db.collection('tutorial')

    def getAllTutorials(self):
        """
        Retrieve all tutorials
        """
        tutorial = [tutorial.to_dict() for tutorial in self.tutorial_db.stream()]
        return tutorial
    
    def getTutorialById(self, id):
        """
        Retrieve Tutorial by ID, if record does not exist, raise Assertion Error
        """
        if self.tutorial_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            tutorial = self.tutorial_db.document(id).get().to_dict()
            return tutorial
    
    def addTutorial(self, id, tutorial_json):
        """
        Add Tutorial into Database, if record already exists, raise Assertin Error
        """
        if self.tutorial_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            tutorial_json["completed"] = json.loads(tutorial_json["completed"])
            tutorial_json["content"] = json.loads(tutorial_json["content"])
            self.tutorial_db.document(id).set(tutorial_json)

    def updateTutorial(self, id, tutorial_json):
        """
        Update Tutorial in Database, if record not found in database, raise Assertion Error
        """
        if self.tutorial_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            tutorial_json["completed"] = json.loads(tutorial_json["completed"])
            tutorial_json["content"] = json.loads(tutorial_json["content"])
            self.tutorial_db.document(id).update(tutorial_json)

    def deleteTutorial(self, id):
        """
        Delete Tutorial from database. If it does not exist, raise Assertion Error
        """
        if self.tutorial_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.tutorial_db.document(id).delete()