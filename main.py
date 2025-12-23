from database.content import ContentDatabase
from database.user import UserDatabase
from database.quiz import QuizDatabase
from database.tutorial import TutorialDatabase
from database.learning_module import LearningModuleDatabase
from database.tutorial_quiz import TutorialQuizDatabase
from database.challenge import ChallengeDatabase

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login_page():
    return "<p>Login Page</p>"

class ContentService(Resource):

    @app.route("/getAllContent", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllContents():
        try:
            content = contents.getAllContent()
            return jsonify(content)
        except Exception as e:
            return str(e), 400
        
    @app.route("/getContentById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getContentById():
        try:
            contentId = request.args.get('id')
            content = contents.getContentById(contentId)
            return jsonify(content), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addContent", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addContent():
        try:
            contentId = request.json['id']
            contents.addContent(contentId, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Content Exists in DB", 400
        except Exception as e:
            return f"An Error Occured: {e}", 400
        
    @app.route("/updateContent", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateContent():
        try:
            contentId = request.json['id']
            contents.updateContent(contentId, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Content Does Not Exist in DB", 400
        except Exception as e:
            return f"An Error Occured: {e}", 400
        
    @app.route("/deleteContent", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteContent():
        try:
            contentId = request.json['id']
            contents.deleteContent(contentId)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Content Does Not Exist in DB", 400
        except Exception as e:
            return f"An Error Occured: {e}", 400
        
class QuizService(Resource):

    @app.route("/getAllQuizzes", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllQuizzes():
        try:
            quiz = quizzes.getAllQuizzes()
            return jsonify(quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getQuizById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getQuizById():
        try:
            quiz_id = request.args.get('id')
            quiz = quizzes.getQuizById(quiz_id)
            return jsonify(quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addQuiz():
        try:
            quiz_id = request.json['id']
            quizzes.addQuiz(quiz_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Quiz Exists in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateQuiz():
        try:
            quiz_id = request.json['id']
            quizzes.updateQuiz(quiz_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Quiz Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/deleteQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteQuiz():
        try:
            quiz_id = request.json['id']
            quizzes.deleteQuiz(quiz_id)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Quiz Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
class TutorialService(Resource):

    @app.route("/getAllTutorials", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllTutorials():
        try:
            tutorial = tutorials.getAllTutorials()
            return jsonify(tutorial), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getTutorialById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getTutorialById():
        try:
            tutorial_id = request.args.get('id')
            tutorial = tutorials.getTutorialById(tutorial_id)
            return jsonify(tutorial), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addTutorial", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addTutorial():
        try:
            tutorial_id = request.json['id']
            tutorials.addTutorial(tutorial_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Tutorial Exists in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateTutorial", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateTutorial():
        try:
            tutorial_id = request.json['id']
            tutorials.updateTutorial(tutorial_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Tutorial Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/deleteTutorial", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteTutorial():
        try:
            tutorial_id = request.json['id']
            tutorials.deleteTutorial(tutorial_id)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Tutorial Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
class ChallengeService(Resource):

    @app.route("/getAllChallenges", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllChallenges():
        try:
            challenge = challenges.getAllChallenges()
            return jsonify(challenge), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getChallengeById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getChallengeById():
        try:
            challenge_id = request.args.get('id')
            challenge = challenges.getChallengeById(challenge_id)
            return jsonify(challenge), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addChallenge", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addChallenge():
        try:
            challenge_id = request.json['id']
            challenges.addChallenge(challenge_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Challenge Exists in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateChallenge", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateChallenge():
        try:
            challenge_id = request.json['id']
            challenges.updateChallenge(challenge_id, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Challenge Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/deleteChallenge", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteChallenge():
        try:
            challenge_id = request.json['id']
            challenges.deleteChallenge(challenge_id)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "Challenge Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
class LearningModuleService(Resource):

    @app.route("/getAllLearningModules", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllLearningModules():
        try:
            learning_module = learning_modules.getAllLearningModules()
            return jsonify(learning_module), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getLearningModuleById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getLearningModuleById():
        try:
            learning_module_id = request.args.get('id')
            learning_module = learning_modules.getLearningModuleById(learning_module_id)
            return jsonify(learning_module), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addLearningModule", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addLearningModule():
        try:
            leaning_module_id = request.json['id']
            learning_modules.addLearningModule(leaning_module_id, request.json)
            return jsonify({"result": True}), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateLearningModule", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateLearningModule():
        try:
            leaning_module_id = request.json['id']
            learning_modules.updateLearningModule(leaning_module_id, request.json)
            return jsonify({"result": True}), 200
        except Exception as e:
            return str(e), 400
    
    @app.route("/deleteLearningModule", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteLearningModule():
        try:
            leaning_module_id = request.json['id']
            learning_modules.deleteLearningModule(leaning_module_id)
            return jsonify({"result": True}), 200
        except Exception as e:
            return str(e), 400
        
class TutorialQuizService(Resource):

    @app.route("/getAllTutorialQuizzes", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllTutorialQuizzes():
        try:
            tutorial_quiz = tutorial_quizzes.getAllTutorialQuizzes()
            return jsonify(tutorial_quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getTutorialQuizById", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getTutorialQuizById():
        try:
            tutorial_quiz_id = request.args.get('id')
            tutorial_quiz = tutorial_quizzes.getTutorialQuizById(tutorial_quiz_id)
            return jsonify(tutorial_quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getTutorialQuizByQuizId", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def getTutorialQuizByQuizId():
        try:
            tutorial_quiz_id = request.json['quizId']
            tutorial_quiz = tutorial_quizzes.getTutorialQuizByQuizId(tutorial_quiz_id)
            return jsonify(tutorial_quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getTutorialQuizByTutorialId", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def getTutorialQuizByTutorialId():
        try:
            tutorial_quiz_id = request.json['tutorialId']
            tutorial_quiz = tutorial_quizzes.getTutorialQuizByTutorialId(tutorial_quiz_id)
            return jsonify(tutorial_quiz), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addTutorialQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addTutorialQuiz():
        try:
            tutorial_quiz_id = request.json['id']
            tutorial_quizzes.addTutorialQuiz(tutorial_quiz_id, request.json)
            return jsonify({"return": True}), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateTutorialQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateTutorialQuiz():
        try:
            tutorial_quiz_id = request.json['id']
            tutorial_quizzes.updateTutorialQuiz(tutorial_quiz_id, request.json)
            return jsonify({"return": True}), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/deleteTutorialQuiz", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteTutorialQuiz():
        try:
            tutorial_quiz_id = request.json['id']
            tutorial_quizzes.deleteTutorialQuiz(tutorial_quiz_id)
            return jsonify({"return": True}), 200
        except Exception as e:
            return str(e), 400
        
class UserService(Resource):

    @app.route("/getAllUsers", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getAllUsers():
        try:
            user = users.getAllUsers()
            return jsonify(user)
        except Exception as e:
            return str(e), 400
        
    @app.route("/getUserByUsername", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getUserByUsername():
        try:
            username = request.json['username']
            user = users.getUserByUsername(username)
            return jsonify(user)
        except Exception as e:
            return str(e), 400
        
    @app.route("/getUsersByRole", methods=['GET'])
    @cross_origin(supports_credentials=True)
    def getUserByRole():
        try:
            roleId = request.json['role']
            role = users.getUsersByRole(roleId)
            return jsonify(role), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/getUserByEmail", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def getUserByEmail():
        try:
            emails = request.json['email']
            email = users.getUserByEmail(emails)
            return jsonify(email), 200
        except Exception as e:
            return str(e), 400
        
    @app.route("/addUser", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def addUser():
        try:
            new_username = request.json['username']
            users.addUser(new_username, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "User Exists in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/updateUser", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def updateUser():
        try:
            old_username = request.json['oldUsername']
            new_username = request.json['username']
            users.updateUser(old_username, new_username, request.json)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "User Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400
        
    @app.route("/deleteUser", methods=['POST'])
    @cross_origin(supports_credentials=True)
    def deleteUser():
        try:
            username = request.json['username']
            users.deleteUser(username)
            return jsonify({"success": True}), 200
        except AssertionError:
            return "User Does Not Exist in DB", 400
        except Exception as e:
            return str(e), 400

if __name__ == "__main__":
    contents = ContentDatabase()
    users = UserDatabase()
    quizzes = QuizDatabase()
    tutorials = TutorialDatabase()
    challenges = ChallengeDatabase()
    learning_modules = LearningModuleDatabase()
    tutorial_quizzes = TutorialQuizDatabase()
    app.run(debug=True)