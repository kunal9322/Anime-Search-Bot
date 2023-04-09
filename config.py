import os


#ForceSub
MUST_JOIN = os.environ.get("MUST_JOIN", "")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
