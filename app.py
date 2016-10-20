from database import Database
from user import User

Database.initialise()

user = User('joseisstupid@wtf.com', 'Jose', 'Stupid', None)

user.save_to_db()

user_from_db = User.load_from_db_by_email('bazinga88@gmail.com')

print(user_from_db)
