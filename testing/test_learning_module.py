import requests

link = "http://127.0.0.1:5000/"

class TestLearningModule:

    """
    Test Module in Learning Module Database
    """

    def test_getAllLearningModules(self):
        """
        getAllLearningModules Test Method
        Input: None

        Case: Call getAllLearningModules Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllLearningModules")
        assert request_obj.status_code == 200

    def test_addLearningModule(self):
        """
        addLearningModule Test Method
        Input: JSON Object with params (id, challengeId, name, description, questions, totalExperiencePoints)

        Case 1: Add Learning Module where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Learning Module where existing ID exists (Negative)
        Expected Status Code 1: 400
        """
        learning_module_json = {
            "id": "10001",
            "challengeId": 1,
            "name": "Learning Module 100",
            "description": "very good learning module",
            "questions": [1],
            "totalExperiencePoints": 70,
        }
        # Case 1: Adding New Learning Module where no existing ID exist
        # Since it's a new Learning Module we're adding, database must never have another
        # Learning Module with the same ID since that case will be handled when updating
        # Learning Modules
        request_obj = requests.post(url=link + "addLearningModule", json=learning_module_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New Learning Module where no existing ID exist
        # Since an Learning Module with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addLearningModule", json=learning_module_json)
        assert request_obj.status_code == 400

    def test_deleteLearningModule(self):
        """
        deleteLearningModule Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Learning Module where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Learning Module where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """
        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addLearningModule would have already added the
        # Learning Module with the respective ID into the database
        learning_module_id = { "id": "10001" }

        # Case 1: Delete Learning Module where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteLearningModule", json=learning_module_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Learning Module where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteLearningModule", json=learning_module_id)
        assert request_obj.status_code == 400

    def test_updateLearningModule(self):
        """
        updateLearningModule Test Method
        Input 2: JSON Object with params (id, challengeId, name, description, questions, totalExperiencePoints)
        Input 1: JSON Object with params (id, challengeId, name, description, questions, totalExperiencePoints)

        Case: Insert Input 1 as Learning Module and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """
        # Initial JSON to be added into Learning Module
        learning_module_json = {
            "id": "10001",
            "challengeId": 1,
            "name": "Learning Module 100",
            "description": "very good learning module",
            "questions": [1],
            "totalExperiencePoints": 70,
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        learning_module_update_json = {
            "id": "10001",
            "challengeId": 1,
            "name": "Learning Module 80",
            "description": "very not so good learning module",
            "questions": [1,4,5],
            "totalExperiencePoints": 100,
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addLearningModule", json=learning_module_json)
        request_obj = requests.post(url=link + "updateLearningModule", json=learning_module_update_json)
        assert request_obj.status_code == 200
        learning_module_id = { "id": "10001" }
        requests.post(url=link + "deleteLearningModule", json=learning_module_id)

    def test_getLearningModuleById(self):
        """
        getLearningModuleById Test Method
        Input 1: JSON Object with params (id, challengeId, name, description, questions, totalExperiencePoints)
        Input 2: JSON Object with params (id)

        Case 1: Get Learning Module according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200
        """

        # Learning Module JSON Object with testing data
        learning_module_json = {
            "id": "10001",
            "challengeId": 1,
            "name": "Learning Module 100",
            "description": "very good learning module",
            "questions": [1],
            "totalExperiencePoints": 70,
        }

        # Testing Object's corresponding ID
        learning_module_id = { "id": "10001" }

        # Case 1: Get Learning Module according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Learning Module from database with the
        # corresponding ID
        requests.post(url=link + "addLearningModule", json=learning_module_json)
        request_obj = requests.post(url=link + "getLearningModuleById", json=learning_module_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteLearningModule", json=learning_module_id)