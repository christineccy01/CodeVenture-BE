import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter
import json

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
quiz_app = firebase_admin.initialize_app(cred, name="quiz_db")
db = firestore.client(quiz_app)

class QuizDatabase:

    def __init__(self):
        self.quiz_db = db.collection('quiz')

    def getAllQuizzes(self):
        """
        Retrieve all quizzes
        """
        quizzes = [quiz.to_dict() for quiz in self.quiz_db.stream()]
        return quizzes
    
    def getQuizById(self, id):
        """
        Retrieve Quiz by ID, if record does not exist, raise Assertion Error
        """
        if self.quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            quiz = self.quiz_db.document(id).get().to_dict()
            return quiz
    
    def addQuiz(self, id, quiz_json):
        """
        Add Quiz into Database, if record already exists, raise Assertin Error
        """
        if self.quiz_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            self.quiz_db.document(id).set(quiz_json)

    def updateQuiz(self, id, quiz_json):
        """
        Update Quiz in Database, if record not found in database, raise Assertion Error
        """
        if self.quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            quiz_json["completed"] = json.loads(quiz_json["completed"])
            quiz_json["content"] = json.loads(quiz_json["content"])
            self.quiz_db.document(id).update(quiz_json)

    def deleteQuiz(self, id):
        """
        Delete Quiz from database. If it does not exist, raise Assertion Error
        """
        if self.quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.quiz_db.document(id).delete()