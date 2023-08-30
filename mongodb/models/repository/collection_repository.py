from typing import List, Dict

class mongoRepository:

    def __init__(self, db_connection) -> None:
        self.__collection_name = "ceiaCollection"
        self.__db_connection = db_connection
    
    def insert_document(self, document: Dict) -> Dict:
        ceiaCollection = self.__db_connection.get_collection(self.__collection_name)
        ceiaCollection.insert_one(document)
        return document

    def delete_document(self,filter: Dict) -> None:
        ceiaCollection = self.__db_connection.get_collection(self.__collection_name)
        ceiaCollection.delete_many(filter)



