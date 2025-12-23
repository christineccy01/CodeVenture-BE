import requests

link = "http://127.0.0.1:5000/"

class TestTutorialQuiz:

    """
    Test Module in Tutorial Quiz Database
    """

    def test_getAllTutorialQuizzes(self):
        """
        getAllTutorialQuizzes Test Method
        Input: None

        Case: Call getAllTutorialQuizzes Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllTutorialQuizzes")
        assert request_obj.status_code == 200

    def test_addTutorialQuiz(self):
        """
        addTutorialQuiz Test Method
        Input: JSON Object with params (id, quizId, tutorialId)

        Case 1: Add Tutorial Quiz where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Tutorial Quiz where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        tutorial_quiz_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 1,
        }

        # Case 1: Adding New Tutorial Quiz where no existing ID exist
        # Since it's a new Tutorial Quiz we're adding, database must never have another
        # Tutorial Quiz with the same ID since that case will be handled when updating
        # Tutorial Quizzes
        request_obj = requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New Tutorial Quiz where no existing ID exist
        # Since an Tutorial Quiz with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        assert request_obj.status_code == 400

    def test_deleteTutorialQuiz(self):

        """
        deleteTutorialQuiz Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Tutorial Quiz where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Tutorial Quiz where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """

        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addTutorialQuiz would have already added the
        # Tutorial Quiz with the respective ID into the database
        tutorial_quiz_id = { "id": "10001" }

        # Case 1: Delete Tutorial Quiz where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Tutorial Quiz where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)
        assert request_obj.status_code == 400

    def test_updateTutorialQuiz(self):

        """
        updateTutorialQuiz Test Method
        Input 1: JSON Object with params (id, quizId, tutorialId)
        Input 2: JSON Object with params (id, quizId, tutorialId)

        Case: Insert Input 1 as Tutorial Quiz and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into tutorial quiz
        tutorial_quiz_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 1
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        tutorial_quiz_update_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 3
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        request_obj = requests.post(url=link + "updateTutorialQuiz", json=tutorial_quiz_update_json)
        assert request_obj.status_code == 200
        tutorial_quiz_id = { "id": "10001" }
        requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)

    def test_getTutorialQuizById(self):

        """
        getTutorialQuizById Test Method
        Input 1: JSON Object with params (id, quizId, tutorialId)
        Input 2: JSON Object with params (id)

        Case 1: Get Tutorial Quiz according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Tutorial Quiz according to ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Tutorial Quiz JSON Object with testing data
        tutorial_quiz_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 1
        }

        # Testing Object's corresponding ID
        tutorial_quiz_id = { "id": "10001" }

        # Case 1: Get Tutorial Quiz according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Tutorial Quiz from database with the
        # corresponding ID
        requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        request_obj = requests.post(url=link + "getTutorialQuizById", json=tutorial_quiz_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)

    def test_getTutorialQuizByQuizId(self):

        """
        getTutorialQuizByQuizId Test Method
        Input 1: JSON Object with params (id, quizId, tutorialId)
        Input 2: JSON Object with params (quizId)

        Case 1: Get Tutorial Quiz according to Quiz ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Tutorial Quiz according to Quiz ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Tutorial Quiz JSON Object with testing data
        tutorial_quiz_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 1
        }
        
        # Testing Object's corresponding ID
        tutorial_quiz_id = { "id": "10001" }

        # Testing Object's corresponding quiz ID
        quiz_id = { "quizId": 1 }

        # Case 1: Get Tutorial Quiz according to Class ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Tutorial Quiz from database with the
        # corresponding Class ID
        requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        request_obj = requests.post(url=link + "getTutorialQuizByQuizId", json=quiz_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)

        # TODO: add negative case

    def test_getTutorialQuizByTutorialId(self):

        """
        getTutorialQuizByTutorialId Test Method
        Input 1: JSON Object with params (id, quizId, tutorialId)
        Input 2: JSON Object with params (tutorialId)

        Case 1: Get Tutorial Quiz according to Tutorial ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Tutorial Quiz according to Tutorial ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Tutorial Quiz JSON Object with testing data
        tutorial_quiz_json = {
            "id": "10001",
            "quizId": 1,
            "tutorialId": 1
        }

        # Testing Object's corresponding ID
        tutorial_quiz_id = { "id": "10001" }

        # Testing Object's corresponding tutorial ID
        tutorial_id = { "tutorialId": 1 }

        # Case 1: Get Tutorial Quiz according to Tutorial ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Tutorial Quiz from database with the
        # corresponding Tutorial ID
        requests.post(url=link + "addTutorialQuiz", json=tutorial_quiz_json)
        request_obj = requests.post(url=link + "getTutorialQuizByTutorialId", json=tutorial_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteTutorialQuiz", json=tutorial_quiz_id)

        # TODO: add negative case