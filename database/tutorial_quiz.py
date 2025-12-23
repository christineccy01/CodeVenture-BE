import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
tutorial_quiz_app = firebase_admin.initialize_app(cred, name="tutorial_quiz_db")
db = firestore.client(tutorial_quiz_app)

class TutorialQuizDatabase:

    def __init__(self):
        self.tutorial_quiz_db = db.collection('tutorial_quiz')

    def getAllTutorialQuizzes(self):
        """
        Retrieve all TutorialQuizzes
        """
        tutorial_quizzes = [tutorial_quiz.to_dict() for tutorial_quiz in self.tutorial_quiz_db.stream()]
        return tutorial_quizzes
    
    def getTutorialQuizById(self, id):
        """
        Retrieve TutorialQuiz by ID, if record does not exist, raise Assertion Error
        """
        if self.tutorial_quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            tutorial_quiz = self.tutorial_quiz_db.document(id).get().to_dict()
            return tutorial_quiz
    
    def getTutorialQuizByTutorialId(self, tutorial_id):
        """
        Retrieve TutorialQuiz by Tutorial ID, if record does not exist, raise Assertion Error
        """
        tutorial_quiz_query = self.tutorial_quiz_db.where(filter=FieldFilter("tutorialId", "==", int(tutorial_id))).stream()
        tutorial_quizzes = [tutorial_quiz.to_dict() for tutorial_quiz in tutorial_quiz_query]
        if tutorial_quizzes == []:
            raise AssertionError
        else:
            return tutorial_quizzes
    
    def getTutorialQuizByQuizId(self, quiz_id):
        """
        Retrieve TutorialQuiz by Quiz ID, if record does not exist, raise Assertion Error
        """
        tutorial_quiz_query = self.tutorial_quiz_db.where(filter=FieldFilter("quizId", "==", int(quiz_id))).stream()
        tutorial_quizzes = [tutorial_quiz.to_dict() for tutorial_quiz in tutorial_quiz_query]
        if tutorial_quizzes == []:
            raise AssertionError
        else:
            return tutorial_quizzes
    
    def addTutorialQuiz(self, id, tutorial_quiz_json):
        """
        Add TutorialQuiz into Database, if record already exists, raise Assertin Error
        """
        if self.tutorial_quiz_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            self.tutorial_quiz_db.document(id).set(tutorial_quiz_json)

    def updateTutorialQuiz(self, id, tutorial_quiz_json):
        """
        Update TutorialQuiz in Database, if record not found in database, raise Assertion Error
        """
        if self.tutorial_quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.tutorial_quiz_db.document(id).update(tutorial_quiz_json)

    def deleteTutorialQuiz(self, id):
        """
        Delete TutorialQuiz from database. If it does not exist, raise Assertion Error
        """
        if self.tutorial_quiz_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.tutorial_quiz_db.document(id).delete()