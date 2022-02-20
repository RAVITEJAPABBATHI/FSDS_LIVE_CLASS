# install pymongo and dnspython
import logging
from MongoAssignment import Mongo_Assignment


def create_logger():
    logging.basicConfig(filename="./Logs/MongoAssignment_Log.txt", level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(message)s', filemode='w')
    logger = logging.getLogger()
    return logger


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyMongo Assignment')
    logger = create_logger()
    mongoAssignment = Mongo_Assignment(logger)
    mongoAssignment.instructions()
    mongoAssignment.perform_Mongo_Assignment()
    logger.info("Thank you")
