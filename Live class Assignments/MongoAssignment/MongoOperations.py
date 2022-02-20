import csv, pymongo
import logging


class Mongo_Operations:
    def __init__(self, logger: logging.Logger, collection: pymongo.collection.Collection):
        """
        This class performs all the mongo operations on the collection provided
        :param logger:
        :param csvfile:
        :param collection:
        """
        self.logger = logger
        self.collection = collection

    def read_csv(self, csvfile):
        """
            Reads csv data in the form of dictionary with delimiter ;
        """
        try:
            reader = csv.DictReader(open(csvfile, 'r'), delimiter=";")
            self.documents = [document for document in reader]
            self.logger.info(f"data from csv {csvfile} read successfully")
        except Exception as e:
            self.logger.error(e)

    def insert_bulk(self):
        """
              Inserts data from documents parameter to mongo db atlas collection
        """
        try:
            self.logger.debug("insert_bulk method")
            result = self.collection.insert_many(self.documents)
            self.logger.info(f"Bulk insert successful")

        except Exception as e:
            self.logger.error(e)

    def insert_one(self, document):
        try:
            self.logger.debug("insert_one method")
            id = self.collection.insert_one(document)
            self.logger.info(f"{id} inserted successfully")

        except Exception as e:
            self.logger.error(e)

    def find_one(self):
        """
               Fetch a single document
        """
        try:
            self.logger.debug("find_one method")
            document = self.collection.find_one()
            print(document)
            self.logger.debug(document)
            self.logger.info(f"one document fetched successfully")

        except Exception as e:
            self.logger.error(e)

    def find_on_filter(self):
        """
        Fetch the document where __id=1
        :return:
        """
        try:
            self.logger.debug("find_on_filter method")
            documents = self.collection.find({"_id": 1})
            for i in documents:
                # print(i)
                self.logger.debug(i)
            self.logger.info(f"documents filtered and fetched successfully using filter '_id': 1 ")

        except Exception as e:
            self.logger.error(e)

    def find_many(self):
        """
               Fetch many documents from collection, limit to 5
        """
        try:
            self.logger.debug("find_many method")
            documents = self.collection.find().limit(5)
            for i in documents:
                # print(i)
                self.logger.debug(i)
            self.logger.info(f"Documents fetched successfully but limited to 5")

        except Exception as e:
            self.logger.error(e)

    def find_on_query(self):
        """
         Fetch many documents on query condition from collection, limit to 5
        """
        try:
            self.logger.debug("find_on_query method")
            query = {"Initial atomic coordinate u": {"$regex": "1$"}}
            documents = self.collection.find(query).limit(5)
            for i in documents:
                # print(i)
                self.logger.debug(i)
            self.logger.info(f"Documents fetched successfully using query :{query}")

        except Exception as e:
            self.logger.error(e)

    def update_one(self):
        """
         update one record in the collection
        """
        try:
            self.logger.debug("update_one method")
            filterCondition = {"Chiral indice n": "2"}
            updateStatement = {"$set": {"Chiral indice n": "0"}}
            document = self.collection.update_one(filterCondition, updateStatement)
            self.logger.debug(document)
            self.logger.info(f"Document:{document.matched_count} updated successfully")

        except Exception as e:
            self.logger.error(e)

    def update_many(self):
        """
         update many in the collection
        """
        try:
            self.logger.debug("update_many method")
            filterCondition = {"Chiral indice m": "1"}
            updateStatement = {"$set": {"Chiral indice m": "0"}}
            result = self.collection.update_many(filterCondition, updateStatement)
            self.logger.debug(result.matched_count)
            self.logger.info(f"Documents:{result.matched_count} updated successfully")

        except Exception as e:
            self.logger.error(e)

    def delete_one(self):
        """
         update one record in the collection
        """
        try:
            self.logger.debug("delete_one method")
            filterCondition = {"_id": 1}
            document = self.collection.delete_one(filterCondition)
            self.logger.debug(document)
            self.logger.info(f"Document:{document.deleted_count} deleted successfully on condition {filterCondition}")

        except Exception as e:
            self.logger.error(e)

    def delete_many(self):
        """
         update many in the collection
        """
        try:
            self.logger.debug("delete_many method")
            filterCondition = {"Chiral indice m": "0"}
            result = self.collection.delete_many(filterCondition)
            self.logger.debug(result.deleted_count)
            self.logger.info(f"Documents:{result.deleted_count} deleted successfully")

        except Exception as e:
            self.logger.error(e)


if __name__ == "MongoOperations":
    print("Mongo Operations object created")
