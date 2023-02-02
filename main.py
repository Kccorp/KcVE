from request import *
from parsing import *
from functions import *
from args import *


def main():
    args = getArgs()

    if not checkArgs(args):
        exit(1)

    startDate = refactorDateFormat(args.startDate)
    endDate = refactorDateFormat(args.endDate)

    if not checkDateRange(startDate, endDate):
        exit(1)

    if identifyWichAPICall(args) == "all":
        # call the api and get the data
        data = callApiAll(startDate, endDate)
    elif identifyWichAPICall(args) == "keyword":
        data = callApiKeyword(startDate, endDate, args.keyword)
    elif identifyWichAPICall(args) == "vendorProduct":
        matchString = createVirtualMatchString(args.vendor, args.product)
        data = callApiVendorProduct(startDate, endDate, matchString)

    # parse the data to a list of cve objects
    cveList = parseDataToCve(data)

    # print all the cve objects
    for i in range(len(cveList)):
        cveList[i].showAll()

    print("\n" + "Total number of CVEs: " + str(len(cveList)))


if __name__ == '__main__':
    main()
