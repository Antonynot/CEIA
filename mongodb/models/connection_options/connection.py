from pymongo import MongoClient

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "mongodb+srv://ceiaproject:ceiaacky12345@cluster0.aqstosu.mongodb.net/?retryWrites=true&w=majority"
        self.__database_name = "ceiaDB"
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        self.__client = MongoClient(self.__connection_string)
        self.__db_connection = self.__client[self.__database_name]

    def get_db_connection(self):
        return self.__db_connection

    def get_db_client(self):
        return self.__client