from pymongo import Connection
import datetime


#Mongodb connection
if __name__ == "__main__":
    con = Connection()
    db = con.boxing_app
    days = db.boxing_app
    days_record = {}


    days_name = raw_input("Enter the date of the day the Muay Thai lesson was taken.")
    days_trainer = raw_input("Enter the trainer for that day.")
    whatwaslearned = raw_input("Enter what was learned that day.")
    keyElements = raw_input("Enter the Key Points I learned that date.")
    days_record = {'day': days_name, 'trainer': days_trainer, 'lesson': whatwaslearned, 'KeyElements': keyElements, 'date': datetime.datetime.utcnow()}
    days.insert(days_record)
    daysinquiry = days.find()

    for dayslisted in daysinquiry:
        print dayslisted