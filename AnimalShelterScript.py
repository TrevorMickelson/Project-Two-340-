from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

class AnimalShelter(object):

    def __init__(self, username, password):

        # This forces the use of the user name and password

        if (not username or not password):

            raise Exception("Error! Could not connect to the database, requires a username and password")



        # Initializing the MongoClient. This helps to 

        # access the MongoDB databases and collections. 

        self.client = MongoClient('mongodb://aacuser:T.13.revor_@localhost:48557/aac')

    

        # where xxxx is your unique port number

        self.database = self.client['aac']

        self.collection = self.database["animals"]



        # Testing authentication
        if (self.database.authenticate(username, password)):

            print("Connection was successful!")

        else:

            raise Exception("Error! The username or password is incorrect!")



        # Validating collection (if not exists, creating one)
        try:

            self.database.validate_collection("animals")  # Try to validate a collection

        except:  # If the collection doesn't exist

            print("This collection doesn't exist...")



    # Complete this create method to implement the C in CRUD.
    def create(self, data):

        if data is not None:

            create = self.collection.insert(data)

            return True if create != 0 else False      

        else:

            raise Exception("Nothing to save, because data parameter is empty")



    # Create method to implement the R in CRUD. 
    def read(self, input):

        try:            
            return self.collection.find(input, {"_id": False})

        except:

            return False

    # Create method to implement the U in CRUD. 
    def update(self, query, new_values):
        if (not query and new_values):
            raise Exception("Error! There must be an input when using the update function")
    
        try:
            return self.collection.update_many(query, new_values)
        except: 
            return False
        
    # Create method to implement the D in CRUD. 
    def delete(self, input):
        if (not input):
            raise Exception("Error! There must be an input when using the delete function")
    
        try:
            return self.collection.delete_many(input)
        except:
            return False