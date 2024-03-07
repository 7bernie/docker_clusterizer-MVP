# models.py

class Application:
    def __init__(self, id, name, dockerfile, status):
        self.id = id
        self.name = name
        self.dockerfile = dockerfile
        self.status = status

    # Other attributes and methods

class ContainerCluster:
    def __init__(self, id, name, application_id, replica_count, status):
        self.id = id
        self.name = name
        self.application_id = application_id
        self.replica_count = replica_count
        self.status = status

    # Other attributes and methods

class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email

    # Other attributes and methods

