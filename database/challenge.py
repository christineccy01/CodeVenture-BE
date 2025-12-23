import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import json

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
challenge_app = firebase_admin.initialize_app(cred, name="challenge_db")
db = firestore.client(challenge_app)

class ChallengeDatabase:

    def __init__(self):
        self.challenge_db = db.collection('challenge')

    def getAllChallenges(self):
        """
        Retrieve all challenges
        """
        challenges = [challenge.to_dict() for challenge in self.challenge_db.stream()]
        return challenges
    
    def getChallengeById(self, id):
        """
        Retrieve Challenge by ID, if record does not exist, raise Assertion Error
        """
        if self.challenge_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            challenge = self.challenge_db.document(id).get().to_dict()
            return challenge
    
    def addChallenge(self, id, challenge_json):
        """
        Add Challenge into Database, if record already exists, raise Assertin Error
        """
        if self.challenge_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            self.challenge_db.document(id).set(challenge_json)

    def updateChallenge(self, id, challenge_json):
        """
        Update Challenge in Database, if record not found in database, raise Assertion Error
        """
        if self.challenge_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            challenge_json["completed"] = json.loads(challenge_json["completed"])
            challenge_json["content"] = json.loads(challenge_json["content"])
            self.challenge_db.document(id).update(challenge_json)

    def deleteChallenge(self, id):
        """
        Delete challenge from database. If it does not exist, raise Assertion Error
        """
        if self.challenge_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.challenge_db.document(id).delete()