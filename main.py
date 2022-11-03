import datetime
from functions import createListofDays, generateDays, convertToDf

startDate = datetime.datetime(2020, 1, 1)
listOfDays = createListofDays(startDate,365)

listOfDaysWithValues = generateDays(listOfDays)
dataFrame = convertToDf(listOfDaysWithValues)



