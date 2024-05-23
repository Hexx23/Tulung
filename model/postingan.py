import json
from lib.db import env_database_id, env_collection_post, database
from appwrite.query import Query
from appwrite.id import ID
class PostinganModel:

    def get_all_post(self):
        request =  database.list_documents(database_id=env_database_id, collection_id=env_collection_post)
        return request['documents']

    def get_by_id(self,id):
        request = database.list_documents(database_id=env_database_id, collection_id=env_collection_post,queries=[Query.equal('$id',id)])
        return request['documents'][0]
    def create_post(self, user_id , image, description):
        document = database.create_document(
            database_id= env_database_id,
            collection_id= env_collection_post,
            document_id= ID.unique(),
            data={
                "Image" : image,
                "Description" : description,
                "user_id" : user_id,
                "Like" : 0,
            }
        )
    def get_by_user(self, user_id):
        request = database.list_documents(database_id=env_database_id, collection_id= env_collection_post, queries=[Query.equal("user_id",user_id)])
        return request['documents']