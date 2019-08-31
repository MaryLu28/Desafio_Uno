import json
import sys
import requests 

def getMissingDates(startDate, endDate, arrayDates):
    startDateArray = startDate.split('-')
    startDateArray = list(map(int, startDateArray))
    endDateArry = endDate.split('-')
    endDateArry = list(map(int, endDateArry))
    missingDates = []
    
    for year in range(startDateArray[0], endDateArry[0]+1):
        for month in range(1, 13):             
            if not ((year == startDateArray[0] and month < startDateArray[1]) or (year == endDateArry[0] and month > endDateArry[1])):
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
        "fechas recibidas": data['fechas'],
        "fechasFaltantes": missingDates
    }
    
    return result

url = 'http://127.0.0.1:8080/periodos/api'
header = {'Accept': 'application/json'}

dataJson = requests.get( url=url, headers=header)
data = dataJson.json()

with open('input.json', 'w') as inputFile:
    json.dump(data, inputFile, indent=4)
    
with open('output.json', 'w') as outputFile:
    json.dump(createResult(data), outputFile, indent=4)