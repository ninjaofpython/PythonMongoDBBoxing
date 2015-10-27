__author__ = 'saamaphinda-lebbie'
from pymongo import Connection
import datetime


#Mongodb connection
if __name__ == "__main__":
    con = Connection()
    db = con.privateTraining
    days = db.privateTraining
    days_record = {}

    #User inputs the date, trainer, what was learned, the schema for the Mongodb, and inserting of the user's data
    days_name = raw_input("Enter the date of the day the personal training was taken.")
    days_trainer = raw_input("Enter the trainer for that day.")
    whatwaslearned = raw_input("Enter what was learned that day.")
    days_record = {'day': days_name, 'trainer': days_trainer, 'lesson': whatwaslearned, 'date': datetime.datetime.utcnow()}
    days.insert(days_record)
    #The the insert and find query of the Mongo database.
    daysinquiry = days.find()
    #Print the results of the query.
    for dayslisted in daysinquiry:
        print dayslisted