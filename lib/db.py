from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.users import Users

client = Client()

env_project_key = '33621dac5bdfec25ac4548cba49a4dd7571a3a3dac84dc57b0d75b8b224af79847680bac7a82e08941ff84fdbf02051d57f32fdd4f2c95d23d16776368a14f6d4485853e4285ff7386bd8e5ef3f90af0e139cb266bba13474ad292830dead739c4a03f234b236f729f48e0d31bce13959d708829e98feedbad487c0a5dbb7e93'
env_project_id = '6623dee392e701845954'
env_database_id = '6623df61359b9d40d34f'
env_collection_post = '6623e051dd7813e8b119'
env_collection_user = '6623df8730c6d0f3af7c'
(client
  .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
  .set_project(env_project_id) # Your project ID
  .set_key(env_project_key) # Your secret API key
  .set_self_signed() # Use only on dev mode with a self-signed SSL cert
)

database = Databases(client)
