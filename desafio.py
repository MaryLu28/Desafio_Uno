import json

def getMissingDates(startDate, endDate, arrayDates):
    startDateArray = startDate.split('-')
    startDateArray = list(map(int, startDateArray))
    endDateArry = endDate.split('-')
    endDateArry = list(map(int, endDateArry))
    datesMissing = []
    
    for year in range(startDateArray[0], endDateArry[0]+1):
        for month in range(1, 13):             
            if not ((year == startDateArray[0] and month < startDateArray[1]) or (year == endDateArry[0] and month >  endDateArry[1])):
                dateAux = str(year)+'-'+str(month).zfill(2)+'-01'
                if dateAux not in arrayDates:
                    datesMissing.append(dateAux)        
                  
    return(datesMissing)

with open('test.json') as dataFile:
    data = json.load(dataFile)

print(getMissingDates(data['fechaCreacion'],data['fechaFin'],data['fechas']))