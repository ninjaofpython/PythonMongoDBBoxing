from pymongo import Connection
import datetime


#Mongodb connection
if __name__ == "__main__":
    con = Connection()
    db = con.boxing_app
    days = db.boxing_app
    days_record = {}

    #User inputs the date, trainer, what was learned, the schema for the Mongodb, and inserting of the user's data
    days_name = raw_input("Enter the date of the day the lesson was taken.")
    days_trainer = raw_input("Enter the trainer for that day.")
    whatwaslearned = raw_input("Enter what was learned that day.")
    keyElements = raw_input("Enter the Key Points that I learned that day.")
    stakTaken = raw_input("Was an Animal Stak taken?")
    datestakTaken = raw_input("Input date of when Animal Stak was taken.")
    days_record = {'day': days_name, 'trainer': days_trainer, 'lesson': whatwaslearned, 'KeyElements': keyElements, 'WasStakTaken': stakTaken, 'DateStakTaken': datestakTaken, 'date': datetime.datetime.utcnow()}
    #The the insert and find query of the Mongo database.
    days.insert(days_record)
    daysinquiry = days.find()
    #Print the results of the query.
    for dayslisted in daysinquiry:
        print dayslisted



