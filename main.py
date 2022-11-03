#import that we need
import datetime
#since we have the functions in another folder,lets import them to main.py
from functions import createListofDays, generateDays, convertToDf

#first set a date            year month day
startDate = datetime.datetime(2020, 1, 1)

#then its time to decide durationin days. we also provide the above stated date
listOfDays = createListofDays(startDate,365)

#now its time to generate the values for each hour of the day for the entire timespan stated above as a list of lists
listOfDaysWithValues = generateDays(listOfDays)

#lets convert our list to a pandas dateframe
dataFrame = convertToDf(listOfDaysWithValues)

#finally we convert our pandas dataframe to a csv file. setting index to False and encoding to utf-8 is optional but
#could help you out later on
dataFrame.to_csv('tempAndHumidity.csv', index=False, encoding='utf-8')

