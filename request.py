import requests as rq

def callApiAll ():
    # api-endpoint
    URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # params given here
    keyword = "Fortinet"
    startDate = "2022-12-01T00:00:00.000"
    endDate = "2023-01-11T00:00:00.000"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'keywordSearch': keyword, 'pubStartDate': startDate, 'pubEndDate': endDate}

    # sending get request and saving the response as response object
    r = rq.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    return data