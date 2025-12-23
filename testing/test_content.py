import requests

link = "http://127.0.0.1:5000/"

class TestContent:

    """
    Test Module in Content Database
    """
    
    def test_getAllContents(self):
        """
        getAllContents Test Method
        Input: None

        Case: Call getAllContents Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllContent")
        assert request_obj.status_code == 200

    
    def test_addContent(self):
        """
        addContent Test Method
        Input: JSON Object with params (id, name, description, experiencePoints, options, solutions)

        Case 1: Add Content where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Content where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        content_json = {
            "id": "10001",
            "name": "Content 20",
            "description": "very nice content",
            "experiencePoints": 70,
            "options": [
                "option a",
                "option b",
                "option c"
            ],
            "solutions": [
                "option b"
            ]
        }

        # Case 1: Adding New Content where no existing ID exist
        # Since it's a new Content we're adding, database must never have another
        # Content with the same ID since that case will be handled when updating
        # Contents
        request_obj = requests.post(url=link + "addContent", json=content_json)
        assert request_obj.status_code == 200


        # Case 2: Adding New Content where no existing ID exist
        # Since an Content with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addContent", json=content_json)
        assert request_obj.status_code == 400

    def test_deleteContent(self):
        """
        deleteContent Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Content where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Content where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """

        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addContent would have already added the
        # Content with the respective ID into the database
        content_id = { "id": "10001" }

        # Case 1: Delete Content where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteContent", json=content_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Content where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteContent", json=content_id)
        assert request_obj.status_code == 400

    
    def test_updateContent(self):
        """
        updateContent Test Method
        Input 1: JSON Object with params (id, name, description, experiencePoints, options, solutions)
        Input 2: JSON Object with params (id, name, description, experiencePoints, options, solutions)

        Case: Insert Input 1 as Content and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into content
        content_json = {
            "id": "10001",
            "name": "Content 20",
            "description": "very nice content",
            "experiencePoints": 70,
            "options": [
                "option a",
                "option b",
                "option c"
            ],
            "solutions": [
                "option b"
            ]
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        content_update_json = {
            "id": "10001",
            "name": "Content 5",
            "description": "very not bad content",
            "experiencePoints": 70,
            "options": [
                "option a",
                "option b"
            ],
            "solutions": [
                "option a"
            ]
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addContent", json=content_json)
        request_obj = requests.post(url=link + "updateContent", json=content_update_json)
        assert request_obj.status_code == 200
        content_id = { "id": "10001" }
        requests.post(url=link + "deleteContent", json=content_id)

    
    def test_getContentById(self):
        """
        getContentById Test Method
        Input 1: JSON Object with params (id, name, description, experiencePoints, options, solutions)
        Input 2: JSON Object with params (id)

        Case 1: Get Content according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Content according to ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Content JSON Object with testing data
        content_json = {
            "id": "10001",
            "name": "Content 20",
            "description": "very nice content",
            "experiencePoints": 70,
            "options": [
                "option a",
                "option b",
                "option c"
            ],
            "solutions": [
                "option b"
            ]
        }

        # Testing Object's corresponding ID
        content_id = {"id":"10001"}

        # Case 1: Get Content according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the Content from database with the
        # corresponding ID
        requests.post(url=link + "addContent", json=content_json)
        request_obj = requests.post(url=link + "getContentById", json=content_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteContent", json=content_id)

        # Case 2: Get Content according to ID listed in Input 2 and record does
        # not exist. Since the record does not exist, we output an error saying that
        # the record is not found in the database
        request_obj = requests.post(url=link + "getContentById", json=content_id)
        assert request_obj.status_code == 400

