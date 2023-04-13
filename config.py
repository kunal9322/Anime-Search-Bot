import os


#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "kunal")

#ForceSub
MUST_JOIN = os.environ.get("MUST_JOIN", "Campus_Bot_Updates")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5885920877").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
