from request import *
from parsing import *
from functions import *
from args import *
from outputBuilder import *


def main():
    args = getArgs()

    if not checkArgs(args):
        exit(1)

    startDate = refactorDateFormat(args.startDate)
    endDate = refactorDateFormat(args.endDate)

    datesList = checkDateRange(startDate, endDate)

    for i in range(1, len(datesList), 2):

        startDate = refactorDateFormat(datesList[i-1].strftime("%Y-%m-%d"))
        endDate = refactorDateFormat(datesList[i].strftime("%Y-%m-%d"))

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

        # exit if no cve found
        if len(cveList) == 0:
            print("\033[91m" + "No CVE found for the given parameters" + "\033[0m")

        elif args.output is not None:
            # create the report
            createCveReport(cveList, args.output)
        else:
            # print the report
            printAllCveObjects(cveList)


if __name__ == '__main__':
    main()
