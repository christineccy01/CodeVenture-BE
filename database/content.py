import firebase_admin
from firebase_admin import credentials, firestore
import json

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
content_app = firebase_admin.initialize_app(cred, name="content_db")
db = firestore.client(content_app)

class ContentDatabase:

    def __init__(self):
        self.content_db = db.collection("content")
        
    def getAllContent(self):
        """
        Retrieve all contents
        """
        contents = [content.to_dict() for content in self.content_db.stream()]
        return contents

    def getContentById(self, id):
        """
        Retrieve Content by ID, if record does not exist, raise Assertion Error
        """
        if self.content_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            content = self.content_db.document(id).get().to_dict()
            return content
    
    def addContent(self, id, content_json):
        """
        Add Content into Database, if record already exists, raise Assertion Error
        """
        if self.content_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            content_json["completed"] = json.loads(content_json["completed"])
            content_json["options"] = json.loads(content_json["options"])
            content_json["solutions"] = json.loads(content_json["solutions"])
            self.content_db.document(id).set(content_json)

    def updateContent(self, id, content_json):
        """
        Update Content in Database, if record not found in database, raise Assertion Error
        """
        if self.content_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            content_json["completed"] = json.loads(content_json["completed"])
            content_json["options"] = json.loads(content_json["options"])
            content_json["solutions"] = json.loads(content_json["solutions"])
            self.content_db.document(id).update(content_json)

    def deleteContent(self, id):
        """
        Delete Content from database. If it does not exist, raise Assertion Error
        """
        if self.content_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.content_db.document(id).delete()