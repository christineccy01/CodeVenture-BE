import requests

link = "http://127.0.0.1:5000/"

class TestQuiz:

    """
    Test Module in Quiz Database
    """

    def test_getAllQuizzes(self):
        """
        getAllQuizzes Test Method
        Input: None

        Case: Call getAllQuizzes Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllQuizzes")
        assert request_obj.status_code == 200

    def test_addQuiz(self):
        """
        addQuiz Test Method
        Input: JSON Object with params (id, name, duration, content, experiencePoints, overallFeedback)

        Case 1: Add Quiz where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Quiz where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        quiz_json = {
            "id": "10001",
            "name": "Quiz 100",
            "duration": 50,
            "content": [1],
            "experiencePoints": 70,
            "overallFeedback": "very good"
        }

        # Case 1: Adding New Quiz where no existing ID exist
        # Since it's a new Quiz we're adding, database must never have another
        # Quiz with the same ID since that case will be handled when updating
        # Quizzes
        request_obj = requests.post(url=link + "addQuiz", json=quiz_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New Quiz where no existing ID exist
        # Since an Quiz with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addQuiz", json=quiz_json)
        assert request_obj.status_code == 400

    def test_deleteQuiz(self):
        """
        deleteQuiz Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Quiz where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Quiz where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """

        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addQuizwould have already added the
        # Quiz with the respective ID into the database
        quiz_id = { "id": "10001" }

        # Case 1: Delete Quiz where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteQuiz", json=quiz_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Quiz where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteQuiz", json=quiz_id)
        assert request_obj.status_code == 400

    def test_updateQuiz(self):
        """
        updateQuiz Test Method
        Input 1: JSON Object with params (id, name, duration, content, experiencePoints, overallFeedback)
        Input 2: JSON Object with params (id, name, duration, content, experiencePoints, overallFeedback)

        Case: Insert Input 1 as Quiz and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into quiz
        quiz_json = {
            "id": "10001",
            "name": "Quiz 100",
            "duration": 50,
            "content": [1],
            "experiencePoints": 70,
            "overallFeedback": "very good"
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        quiz_update_json = {
            "id": "10001",
            "name": "Quiz 90",
            "duration": 50,
            "content": [1,2,3],
            "experiencePoints": 100,
            "overallFeedback": "very not so good"
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addQuiz", json=quiz_json)
        request_obj = requests.post(url=link + "updateQuiz", json=quiz_update_json)
        assert request_obj.status_code == 200
        quiz_id = { "id": "10001" }
        requests.post(url=link + "deleteQuiz", json=quiz_id)

    def test_getQuizById(self):
        """
        getQuizById Test Method
        Input 1: JSON Object with params (id, name, duration, content, experiencePoints, overallFeedback)
        Input 2: JSON Object with params (id)

        Case 1: Get Quiz according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200
        """

        # Quiz JSON Object with testing data
        quiz_json = {
            "id": "10001",
            "name": "Quiz 100",
            "duration": 50,
            "content": [1],
            "experiencePoints": 70,
            "overallFeedback": "very good"
        }

        # Testing Object's corresponding ID
        quiz_id = { "id": "10001" }

        # Case 1: Get Quiz according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Quiz from database with the
        # corresponding ID
        requests.post(url=link + "addQuiz", json=quiz_json)
        request_obj = requests.post(url=link + "getQuizById", json=quiz_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteQuiz", json=quiz_id)