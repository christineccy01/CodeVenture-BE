import requests

link = "http://127.0.0.1:5000/"

class TestClass:

    """
    Test Module in Class Database
    """

    def test_getAllClasses(self):
        """
        getAllClasses Test Method
        Input: None

        Case: Call getAllClasses Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllClasses")
        assert request_obj.status_code == 200

    def test_addClass(self):

        """
        addClass Test Method
        Input: JSON Object with params (id, name, teacherId, assignments, enrolledStudents)

        Case 1: Add Class where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add Class where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        class_json = {
            "id": "10001",
            "name": "Class 100",
            "teacherId": 1,
            "assignments": [
                1
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003"
            ]
        }

        # Case 1: Adding New Class where no existing ID exist
        # Since it's a new class we're adding, database must never have another
        # class with the same ID since that case will be handled when updating
        # classes
        request_obj = requests.post(url=link + "addClass", json=class_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New Class where no existing ID exist
        # Since an class with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addClass", json=class_json)
        assert request_obj.status_code == 400

    def test_deleteClass(self):

        """
        deleteClass Test Method
        Input: JSON Object with params (id)

        Case 1: Delete Class where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete Class where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """

        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addClass would have already added the
        # Class with the respective ID into the database
        content_id = { "id": "10001" }

        # Case 1: Delete Class where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteClass", json=content_id)
        assert request_obj.status_code == 200

        # Case 2: Delete Class where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteClass", json=content_id)
        assert request_obj.status_code == 400

    def test_updateClass(self):

        """
        updateClass Test Method
        Input 1: JSON Object with params (id, name, teacherId, assignments, enrolledStudents)
        Input 2: JSON Object with params (id, name, teacherId, assignments, enrolledStudents)

        Case: Insert Input 1 as Class and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into assignment
        class_json = {
            "id": "10001",
            "name": "Class 100",
            "teacherId": 1,
            "assignments": [
                1
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003"
            ]
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        class_update_json = {
            "id": "10001",
            "name": "Class 90",
            "teacherId": 1,
            "assignments": [
                3
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003",
                "mtan0014"
            ]
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addClass", json=class_json)
        request_obj = requests.post(url=link + "updateClass", json=class_update_json)
        assert request_obj.status_code == 200
        class_id = { "id": "10001" }
        requests.post(url=link + "deleteClass", json=class_id)

    def test_getClassById(self):

        """
        getClassById Test Method
        Input 1: JSON Object with params (id, name, teacherId, assignments, enrolledStudents)
        Input 2: JSON Object with params (id)

        Case 1: Get Class according to ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Class according to ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Assignment JSON Object with testing data
        class_json = {
            "id": "10001",
            "name": "Class 100",
            "teacherId": 1,
            "assignments": [
                1
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003"
            ]
        }

        # Testing Object's corresponding ID
        class_id = {"id":"10001"}

        # Case 1: Get Class according to ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the class from database with the
        # corresponding ID
        requests.post(url=link + "addClass", json=class_json)
        request_obj = requests.post(url=link + "getClassById", json=class_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteClass", json=class_id)

        # Case 2: Get Class according to ID listed in Input 2 and record does not
        # exist. since record cannot be found in the database, no object will be
        # returned
        request_obj = requests.post(url=link + "getClassById", json=class_id)
        assert request_obj.status_code == 400

    def test_getClassByTeacherId(self):

        """
        getAssignmentByTeacherId Test Method
        Input 1: JSON Object with params (id, name, teacherId, assignments, enrolledStudents)
        Input 2: JSON Object with params (teacherId)

        Case 1: Get Assignment according to Teacher ID listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200

        Case 2: Get Assignment according to Teacher ID listed in Input 2 and record does not exists (Negative)
        Expected Status Code 2: 400
        """

        # Assignment JSON Object with testing data
        class_json = {
            "id": "10001",
            "name": "Class 100",
            "teacherId": 5,
            "assignments": [
                1
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003"
            ]
        }

        # Testing Object's corresponding Teacher ID
        teacher_id = { "teacherId": 5 }

        # Testing Object's corresponding ID
        class_id = { "id": "10001" }

        # Case 1: Get Assignment according to Class ID listed in Input 2 and record exists
        # Since record exists, we can retrieve the assignment from database with the
        # corresponding Class ID    
        requests.post(url=link + "addClass", json=class_json)
        request_obj = requests.post(url=link + "getClassByTeacherId", json=teacher_id)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteClass", json=class_id)

        request_obj = requests.post(url=link + "getClassByTeacherId", json=teacher_id)
        assert request_obj.status_code == 400

    def test_manageEnrolledStudents(self):
        class_json = {
            "id": "10001",
            "name": "Class 100",
            "teacherId": 5,
            "assignments": [
                1
            ],
            "enrolledStudents": [
                "mche0121",
                "ctan0003"
            ]
        }
        
        class_update_json = {
            "id": "10001",
            "enrolledStudents": [
                "ayon0039",
                "mche0121"
            ]
        }

        class_id = { "id": "10001" }

        requests.post(url=link + "addClass", json=class_json)
        request_obj = requests.post(url=link + "addEnrolledStudent", json=class_update_json)
        assert request_obj.status_code == 200

        request_obj = requests.post(url=link + "deleteEnrolledStudent", json=class_update_json)
        assert request_obj.status_code == 200

        requests.post(url=link + "deleteClass", json=class_id)