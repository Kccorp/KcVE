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

    # call the api and get the data
    data = callApiAll(startDate, endDate)

    # parse the data to a list of cve objects
    cveList = parseDataToCve(data)

    # print all the cve objects
    for i in range(len(cveList)):
        cveList[i].showAll()


if __name__ == '__main__':
    main()
