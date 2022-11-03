import datetime
import random
import pandas as pd


def createListofDays(startDate:datetime, nrOfDays:int):
    dt = startDate
    step = datetime.timedelta(days=1)

    result = []

    while len(result) < nrOfDays:
        result.append(dt)
        dt += step
    
    return result

def generateDays(listWithDates):

    listOfTimeWithValues =[]
    indoorTemp = 23.1
    inbdoorHumidity = 26.0  

    for day in listWithDates:
        date = day
        for hour in range(0,23):
            date = date + datetime.timedelta(hours=1)
            if indoorTemp < 19.8:
                indoorTemp = indoorTemp + 0.1
            elif indoorTemp > 29.4:
                indoorTemp = indoorTemp - 0.1
            else: 
                indoorTemp = indoorTemp + random.uniform(-0.3, 0.3)

            if inbdoorHumidity < 21.1:
                inbdoorHumidity = inbdoorHumidity + 0.1
            elif inbdoorHumidity > 49.5:
                inbdoorHumidity = inbdoorHumidity - 0.1
            else: 
                inbdoorHumidity = inbdoorHumidity + random.uniform(-0.5, 0.5)

            hourlyReading = [date,indoorTemp,inbdoorHumidity]
            listOfTimeWithValues.append(hourlyReading)
    return listOfTimeWithValues        

def convertToDf(list:list):
    df = pd.DataFrame(list, columns = ['Time', 'Indoor Temperature', 'Indoor Temperature'])
    return df
