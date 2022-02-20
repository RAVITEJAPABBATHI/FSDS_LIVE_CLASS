import pymongo
from MongoOperations import Mongo_Operations


class Mongo_Assignment:
    def __init__(self, logger):
        self.logger = logger

    def instructions(self):
        self.logger.debug("Printing Instructions")
        self.logger.debug(
            """
            1.Visit the link "https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes"
            2. Download the dataset
            3.Insert bulk data(from csv into mongodb)
            4.Different Mongo db operation
            """
        )
        self.logger.info("Printed Instructions")

    def get_Mongo_Collection(self):
        mycol = None
        try:
            self.logger.debug("Connecting to PyMongo client and fetching the db and collection carbon_nanotubes_col")
            client = pymongo.MongoClient(
                "mongodb+srv://mongodb:mongodb@mongodbcluster.ff9uj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
            mydb = client["carbon_nanotubes_db"]
            mycol = mydb["carbon_nanotubes_col"]
            self.logger.info("collection carbon_nanotubes_col fetched successfully")
        except Exception as e:
            self.logger.error(e)
        return mycol

    def drop_Mongo_Collection(self, mycol):
        try:
            self.logger.debug("Dropping the mongo db collection")
            mycol.drop()
            self.logger.info("Dropped the mongo db collection successfully")
        except Exception as e:
            self.logger.error(e)

    def perform_Mongo_Assignment(self):
        try:
            myCollection = self.get_Mongo_Collection()
            mongoOps = Mongo_Operations(self.logger, myCollection)

            mongoOps.read_csv("./Data/carbon_nanotubes.csv")
            # bulk insert 
            mongoOps.insert_bulk()
            self.logger.info('')
            # insert one 
            document = {"_id": 1, "Chiral indice n": "2", "Chiral indice m": "1",
                        "Initial atomic coordinate u": "0,679007", "Initial atomic coordinate v": "0,701378",
                        "Initial atomic coordinate w": "0,017037", "Calculated atomic coordinates u'": "0,721037",
                        "Calculated atomic coordinates v'": "0,730237", "Calculated atomic coordinates w'": "0,017017"}
            mongoOps.insert_one(document)
            self.logger.info('')

            # find one
            mongoOps.find_one()
            self.logger.info('')

            # find on filter condition
            mongoOps.find_on_filter()
            self.logger.info('')

            # find many condition
            mongoOps.find_many()
            self.logger.info('')

            # Query condition
            mongoOps.find_on_query()
            self.logger.info('')

            # update one
            mongoOps.update_one()
            self.logger.info('')

            # update many
            mongoOps.update_many()
            self.logger.info('')

            # delete one
            mongoOps.delete_one()
            self.logger.info('')

            # delete many
            mongoOps.delete_many()
            self.logger.info('')

            # dropping collection
            self.drop_Mongo_Collection(myCollection)
            self.logger.info('')
        except Exception as e:
            self.logger.error(e)


if __name__ == "MongoAssignment":
    print("Mongo Assignment Object created")
