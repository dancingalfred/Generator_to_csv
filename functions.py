import datetime
import random


def createListofDays(startDate:datetime, nrOfDays:int):
    dt = startDate
    step = datetime.timedelta(days=1)

    result = []

    while len(result) < nrOfDays:
        result.append(dt.strftime('%Y-%m-%d %H:%M:%S'))
        dt += step
    
    return result

def generateDays(listWithDates):

    listOfDaysWithValues =[]

    for day in listWithDates:
        date = listWithDates[day]


    pass