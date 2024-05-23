from lib.db import env_database_id, env_collection_user, database
from appwrite.id import ID
from appwrite.query import Query
class AkunProfileModel:
    def create_account(self,email,password,username):
        document = database.create_document(
            database_id = env_database_id,
            collection_id= env_collection_user,
            document_id= ID.unique(),
            data={
                'Email': email,
                'Password': password,
                'Username': username,
            }
        )
    def get_by_email(self,email):
        request = database.list_documents(database_id=env_database_id, collection_id=env_collection_user, queries=[Query.equal('Email',email)])
        if request['total'] == 0:
            return None
        return request['documents'][0]