import requests

link = "http://127.0.0.1:5000/"

class TestTutorial:

    """
    Test Module in Tutorial Database
    """

    def test_getAllTutorials(self):
        """
        getAllTutorials Test Method
        Input: None

        Case: Call getAllTutorials Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllTutorials")
        assert request_obj.status_code == 200

    def test_addTutorial(self):
        """
        addTutorial Test Method
        Input: JSON Object with params (id, name, content, experiencePoints)

        Case 1: Add Tutorial where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Tutorial where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        tutorial_json = {
            "id": "10001",
            "name": "Tutorial 100",
            "content": [1],
            "experiencePoints": 70,
        }

        # Case 1: Adding New Tutorial where no existing ID exist
        # Since it's a new Content we're adding, database must never have another
        # Tutorial with the same ID since that case will be handled when updating
        # Tutorials
        request_obj = requests.post(url=link + "addTutorial", json=tutorial_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New Tutorial where no existing ID exist
        # Since an Tutorial with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addTutorial", json=tutorial_json)
        assert request_obj.status_code == 400

    def test_deleteTutorial(self):
        """
        deleteTutorial Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Tutorial where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Tutorial where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """

        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addTutorial would have already added the
        # Tutorial with the respective ID into the database
        tutorial_id = { "id": "10001" }

        # Case 1: Delete Tutorial where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteTutorial", json=tutorial_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Tutorial where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteTutorial", json=tutorial_id)
        assert request_obj.status_code == 400

    def test_updateTutorial(self):
        """
        updateTutorial Test Method
        Input 1: JSON Object with params (id, name, content, experiencePoints)
        Input 2: JSON Object with params (id, name, content, experiencePoints)

        Case: Insert Input 1 as Tutorial and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into tutorial
        tutorial_json = {
            "id": "10001",
            "name": "Tutorial 100",
            "content": [1],
            "experiencePoints": 70,
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        tutorial_update_json = {
            "id": "10001",
            "name": "Tutorial 90",
            "content": [1,2,3],
            "experiencePoints": 100,
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addTutorial", json=tutorial_json)
        request_obj = requests.post(url=link + "updateTutorial", json=tutorial_update_json)
        assert request_obj.status_code == 200
        tutorial_id = { "id": "10001" }
        requests.post(url=link + "deleteTutorial", json=tutorial_id)

    def test_getTutorialById(self):
        """
        getTutorialById Test Method
        Input 1: JSON Object with params (id, name, content, experiencePoints)
        Input 2: JSON Object with params (id)

        Case 1: Get Tutorial according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Tutorial according to ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Tutorial JSON Object with testing data
        tutorial_json = {
            "id": "10001",
            "name": "Tutorial 100",
            "content": [1],
            "experiencePoints": 70,
        }

        # Testing Object's corresponding ID
        tutorial_id = { "id": "10001" }

        # Case 1: Get Tutorial according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Tutorial from database with the
        # corresponding ID
        requests.post(url=link + "addTutorial", json=tutorial_json)
        request_obj = requests.post(url=link + "getTutorialById", json=tutorial_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteTutorial", json=tutorial_id)