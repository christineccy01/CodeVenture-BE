import requests

link = "http://127.0.0.1:5000/"

class TestUser:

    """
    Test Module in User Database
    """

    def test_getAllUsers(self):
        """
        getAllUsers Test Method
        Input: None

        Case: Call getAllUsers Method
        Expected Status Code: 200
        """
        request_obj = requests.get(url=link + "getAllUsers")
        assert request_obj.status_code == 200

    def test_addUser(self):
        """
        addUser Test Method
        Input: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)

        Case 1: Add User where no existing ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Add User where existing ID exists (Negative)
        Expected Status Code 1: 400
        """

        # JSON object to be added into the database
        user_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0001",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very good person",
            "password": "123456",
            "role": 1,
            "totalExperiencePoints": 100,
        }

        # Case 1: Adding New User where no existing ID exist
        # Since it's a new Content we're adding, database must never have another
        # User with the same ID since that case will be handled when updating
        # Users
        request_obj = requests.post(url=link + "addUser", json=user_json)
        assert request_obj.status_code == 200

        # Case 2: Adding New User where no existing ID exist
        # Since an User with the same ID exist in the database, system shall
        # not allow adding of the input JSON since it will overwrite the current
        # record in the database
        request_obj = requests.post(url=link + "addUser", json=user_json)
        assert request_obj.status_code == 400

    def test_deleteUser(self):
        """
        deleteUser Test Method
        Input: JSON Object with params (id)

        Case 1: Delete User where record with ID exists (Positive)
        Expected Status Code 1: 200

        Case 2: Delete User where no record with ID exists (Negative)
        Expected Status Code 1: 400
        """
        # We assume that a record with id 10001 already exists in the database
        # Since the method test_addContent would have already added the
        # User with the respective ID into the database
        username = { "username": "mhao0001" }

        # Case 1: Delete User where record with ID exists
        # Since record with corresponding ID exists, we can safely
        # delete the record from the database
        request_obj = requests.post(url=link + "deleteUser", json=username)
        assert request_obj.status_code == 200

        # Case 2: Delete User where no record with ID exists
        # Since record with corresponding ID does not exist, no deletion
        # is required towards any database record
        request_obj = requests.post(url=link + "deleteUser", json=username)
        assert request_obj.status_code == 400

    def test_updateUser(self):
        """
        updateUser Test Method
        Input 1: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)
        Input 2: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)

        Case: Insert Input 1 as User and update Input 1 by passing in a new object Input 2 that
                contains the new values where necessary
        Expected Status Code: 200
        """

        # Initial JSON to be added into content
        user_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0001",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very good person",
            "password": "123456",
            "role": 1,
            "totalExperiencePoints": 100,
        }

        # New JSON with updated values where necessary to update
        # an original record in the database
        user_update_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0003",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very not so good person",
            "password": "abc12345",
            "role": 1,
            "totalExperiencePoints": 80,
        }

        # Case: Add Input 1 into database and update it through Input 2
        # Since both objects' ID are the same, Input 2's values will
        # update Input 1's values after Input 1 is added into the database.
        # Then the record is deleted since it's testing data and not live data
        requests.post(url=link + "addUser", json=user_json)
        request_obj = requests.post(url=link + "updateUser", json=user_update_json)
        assert request_obj.status_code == 200
        username = { "username": "mhao0001" }
        requests.post(url=link + "deleteUser", json=username)

    def test_getUserByUsername(self):
        """
        getUserByUsername Test Method
        Input 1: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)
        Input 2: JSON Object with params (username)

        Case: Get User according to username listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200
        """
        # User JSON Object with testing data
        user_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0001",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very good person",
            "password": "123456",
            "role": 1,
            "totalExperiencePoints": 100,
        }

        # Testing Object's corresponding username
        username = { "username": "mhao0001" }

        # Case: Get User according to username listed in Input 2 and record exists
        # Since record exists, we can retrieve the User from database with the
        # corresponding username
        requests.post(url=link + "addUser", json=user_json)
        request_obj = requests.get(url=link + "getUserByUsername", json=username)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteUser", json=username)

    def test_getUserByEmail(self):
        """
        getUserByEmail Test Method
        Input 1: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)
        Input 2: JSON Object with params (username)
        Input 3: JSON Object with params (email)

        Case: Get User according to email listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200
        """
        # User JSON Object with testing data
        user_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0001",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very good person",
            "password": "123456",
            "role": 1,
            "totalExperiencePoints": 100,
        }

        # Testing Object's corresponding username
        username = { "username": "mhao0001" }

        # Testing Object's corresponding email
        email = { "email": "mhao0001@student.monash.edu" }

        # Case: Get User according to username listed in Input 2 and 
        # email in Input 3 record exists. Since record exists, we can 
        # retrieve the User from database with the corresponding username
        # and email
        requests.post(url=link + "addUser", json=user_json)
        request_obj = requests.post(url=link + "getUserByEmail", json=email)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteUser", json=username)


    def test_getUsersByRole(self):
        """
        getUserByRole Test Method
        Input 1: JSON Object with params (oldUsername, username, firstName, lastName, email, bio, password, role, totalExperiencePoints)
        Input 2: JSON Object with params (username)
        Input 3: JSON Object with params (role)

        Case: Get User according to role listed in Input 2 and record exists (Positive)
        Expected Status Code 1: 200
        """
        # User JSON Object with testing data
        user_json = {
            "oldUsername": "mhao0001",
            "username": "mhao0001",
            "firstName": "Mei Hou",
            "lastName": "Hao",
            "email": "mhao0001@student.monash.edu",
            "bio": "very good person",
            "password": "123456",
            "role": 1,
            "totalExperiencePoints": 100,
        }

         # Testing Object's corresponding username
        username = { "username": "mhao0001" }

         # Testing Object's corresponding role
        role = { "role": 1 }

        # Case: Get User according to username listed in Input 2 and 
        # role in Input 3 record exists. Since record exists, we can 
        # retrieve the User from database with the corresponding username
        # and role
        requests.post(url=link + "addUser", json=user_json)
        request_obj = requests.post(url=link + "getUsersByRole", json=role)
        assert request_obj.status_code == 200
        requests.post(url=link + "deleteUser", json=username)