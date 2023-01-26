import requests as rq


def callApiAll(startDate, endDate):
    # api-endpoint
    URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'pubStartDate': startDate, 'pubEndDate': endDate, 'sourceIdentifier': 'nvd@nist.gov'}

    # sending get request and saving the response as response object
    r = rq.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    return data


def callApiKeyword(startDate, endDate, keyword):
    # api-endpoint
    URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'pubStartDate': startDate,
              'pubEndDate': endDate,
              'keywordSearch': keyword,
              'sourceIdentifier': 'nvd@nist.gov'}

    # sending get request and saving the response as response object
    r = rq.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    return data


def callApiVendorProduct(startDate, endDate, virtualMatchString):
    # api-endpoint
    URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'pubStartDate': startDate,
              'pubEndDate': endDate,
              'virtualMatchString': virtualMatchString,
              'sourceIdentifier': 'nvd@nist.gov'}

    # sending get request and saving the response as response object
    r = rq.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = r.json()

    return data
