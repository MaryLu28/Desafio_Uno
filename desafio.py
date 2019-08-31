import json
import sys

def getMissingDates(startDate, endDate, arrayDates):
    startDateArray = startDate.split('-')
    startDateArray = list(map(int, startDateArray))
    endDateArry = endDate.split('-')
    endDateArry = list(map(int, endDateArry))
    missingDates = []
    
    for year in range(startDateArray[0], endDateArry[0]+1):
        for month in range(1, 13):             
            if not ((year == startDateArray[0] and month < startDateArray[1]) or (year == endDateArry[0] and month >  endDateArry[1])):
                dateAux = str(year)+'-'+str(month).zfill(2)+'-01'
                if dateAux not in arrayDates:
                    missingDates.append(dateAux)        
               
    return(missingDates)

def createResult(data):
    missingDates = getMissingDates(data['fechaCreacion'],data['fechaFin'],data['fechas'])
    result = {
        "id": data['id'],
        "fechaCreacion": data['fechaCreacion'],
        "fechaFin": data['fechaFin'],
        "fechasFaltantes": missingDates
    }
    
    return result

with open(sys.argv[1], 'r') as inputFile:
    data = json.load(inputFile)
    
with open(sys.argv[2], 'w') as outputFile:
        json.dump(createResult(data), outputFile, indent=4)

print(createResult(data))