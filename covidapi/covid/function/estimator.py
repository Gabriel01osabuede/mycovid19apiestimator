import json
import math



def estimator(data):
    data = impactEstimator(data)
    return data


def periodInDays(periodtype,value):
    value = int(value)
    if periodtype == 'days':
        return value
    elif periodtype == "weeks":
        return value * 7
    elif periodtype == "months":
        return value * 30


def impactEstimator(data):

    dictData = data

    impact = {}
    severeImpact = {}

    # calculation for impact case
    # currently infected calculations

    currentlyInfected = dictData['reportedCases'] * 10

    # calculation for converting the periodtype into days.
    days = periodInDays(dictData['periodType'],dictData['timeToElapse'])
    factor = (days // 3)

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculating severeCasesByRequestedTime
    severeCasesByRequestedTime = (infectionsByRequestedTime * 15) / 100

    # calculating hospitalBedsByRequestedTime
    totalHospitalBeds = dictData['totalHospitalBeds']
    totalHospitalBeds = (totalHospitalBeds * 35)/100
    hospitalBedsByRequestedTime = totalHospitalBeds - severeCasesByRequestedTime

    # calculating casesForICUByRequestedTime
    casesForICUByRequestedTime = (infectionsByRequestedTime * 5)/100

    # calculating casesForVentilatorsByRequestedTime
    casesForVentilatorsByRequestedTime = (infectionsByRequestedTime * 2)/100

    # calculating dollarsInFlight
    avgDailyIncomeInUSD = dictData['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = dictData['region']['avgDailyIncomePopulation']
    dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD)/days


    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)
    casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)
    dollarsInFlight = math.trunc(dollarsInFlight)


    # adding all data gotten into the dictionary
    impact['currentlyInfected'] = currentlyInfected
    impact['infectionsByRequestedTime'] = infectionsByRequestedTime
    impact['severeCasesByRequestedTime']=severeCasesByRequestedTime
    impact['hospitalBedsByRequestedTime']= hospitalBedsByRequestedTime
    impact['casesForICUByRequestedTime']=casesForICUByRequestedTime
    impact['casesForVentilatorsByRequestedTime']=casesForVentilatorsByRequestedTime
    impact['dollarsInFlight']=dollarsInFlight

    # calculation for severeImpact Cases
    # currently infected calculations
    currentlyInfected = dictData['reportedCases'] * 50

    # calculation for infectionByRequestedTime
    infectionsByRequestedTime = currentlyInfected * (2 ** factor)

    # calculating severeCasesByRequestedTime
    severeCasesByRequestedTime = (infectionsByRequestedTime * 15) / 100

    # calculating hospitalBedsByRequestedTime
    totalHospitalBeds = dictData['totalHospitalBeds']
    totalHospitalBeds = (totalHospitalBeds * 35) / 100
    hospitalBedsByRequestedTime = totalHospitalBeds - severeCasesByRequestedTime

    # calculating casesForICUByRequestedTime

    casesForICUByRequestedTime = (infectionsByRequestedTime * 5)/100

    # calculating casesForVentilatorsByRequestedTime
    casesForVentilatorsByRequestedTime = (infectionsByRequestedTime * 2)/100

    # calculating dollarsInFlight
    avgDailyIncomeInUSD = dictData['region']['avgDailyIncomeInUSD']
    avgDailyIncomePopulation = dictData['region']['avgDailyIncomePopulation']
    dollarsInFlight = (infectionsByRequestedTime * avgDailyIncomePopulation * avgDailyIncomeInUSD)/days

    # removing decimal places
    currentlyInfected = math.trunc(currentlyInfected)
    infectionsByRequestedTime = math.trunc(infectionsByRequestedTime)
    severeCasesByRequestedTime = math.trunc(severeCasesByRequestedTime)
    hospitalBedsByRequestedTime = math.trunc(hospitalBedsByRequestedTime)
    casesForICUByRequestedTime = math.trunc(casesForICUByRequestedTime)
    casesForVentilatorsByRequestedTime = math.trunc(casesForVentilatorsByRequestedTime)
    dollarsInFlight = math.trunc(dollarsInFlight)

    # adding all data to the dicionary
    severeImpact['currentlyInfected'] = currentlyInfected
    severeImpact['infectionsByRequestedTime'] = infectionsByRequestedTime
    severeImpact['severeCasesByRequestedTime'] = severeCasesByRequestedTime
    severeImpact['hospitalBedsByRequestedTime'] = hospitalBedsByRequestedTime
    severeImpact['casesForICUByRequestedTime'] = casesForICUByRequestedTime
    severeImpact['casesForVentilatorsByRequestedTime'] = casesForVentilatorsByRequestedTime
    severeImpact['dollarsInFlight'] = dollarsInFlight

    data = {
        'data': data,
        'impact': impact,
        'severeImpact': severeImpact
    }

    return data
