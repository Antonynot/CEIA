from models.connection_options.connection import DBConnectionHandler
from models.repository.collection_repository import mongoRepository
from datetime import datetime, timedelta

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
db_connection = db_handle.get_db_connection()


ceia_repository = mongoRepository(db_connection)

