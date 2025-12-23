import firebase_admin
from firebase_admin import credentials, firestore

# Auth Credentials
cred = credentials.Certificate("config/firebase-config.json")
learning_module_app = firebase_admin.initialize_app(cred, name="learning_module_db")
db = firestore.client(learning_module_app)

class LearningModuleDatabase:

    def __init__(self):
        self.learning_module_db = db.collection('learning_module')

    def getAllLearningModules(self):
        """
        Retrieve all learning modules
        """
        learning_modules = [learning_module.to_dict() for learning_module in self.learning_module_db.stream()]
        return learning_modules
    
    def getLearningModuleById(self, id):
        """
        Retrieve Learning Module by ID, if record does not exist, raise Assertion Error
        """
        if self.learning_module_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            learning_module = self.learning_module_db.document(id).get().to_dict()
            return learning_module
    
    def addLearningModule(self, id, learning_module_json):
        """
        Add Learning Module into Database, if record already exists, raise Assertin Error
        """
        if self.learning_module_db.document(id).get().to_dict() is not None:
            raise AssertionError
        else:
            self.learning_module_db.document(id).set(learning_module_json)

    def updateLearningModule(self, id, learning_module_json):
        """
        Update Learning Module in Database, if record not found in database, raise Assertion Error
        """
        if self.learning_module_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.learning_module_db.document(id).update(learning_module_json)

    def deleteLearningModule(self, id):
        """
        Delete learning module from database. If it does not exist, raise Assertion Error
        """
        if self.learning_module_db.document(id).get().to_dict() is None:
            raise AssertionError
        else:
            self.learning_module_db.document(id).delete()