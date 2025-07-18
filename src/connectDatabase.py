from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("postgresql://postgres:123456@localhost:5432/postgres")

print(db.get_table_names())