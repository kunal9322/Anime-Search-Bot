import os


#Database 
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://brmhwhgf:Eq_ZuGoNei_j50ST1iGf7WMymc6IO9vf@hattie.db.elephantsql.com/brmhwhgf")
DB_NAME = os.environ.get("DATABASE_NAME", "kunal")

#ForceSub
MUST_JOIN = os.environ.get("MUST_JOIN", "Campus_Bot_Update")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5885920877").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
