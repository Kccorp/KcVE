import re
from datetime import datetime


def checkDateFormat(dateFullString):
    if dateFullString is None:
        return None

    # regex to get the date from the string in the format of YYYY-MM-DD or YYYY/MM/DD or YYYY.MM.DD
    dateRegex = re.compile(r'^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$')

    # if the date is not in the correct format return None
    if dateRegex.search(dateFullString) is None:
        return None

    return dateRegex.search(dateFullString).group()


def checkDateRange(startDate, endDate):
    if startDate is None or endDate is None:
        return False

    # remove T00:00:00.000 from the date
    startDate = startDate.split("T")[0]
    endDate = endDate.split("T")[0]

    # convertir les dates en datetime
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()

    # calculer la différence entre les deux dates
    diff = endDate - startDate

    # si la différence est supérieure à 90 jours retourner false
    if diff.days > 120:
        print("\033[91m" + "The research period is limited to 4 months " + "\033[0m")
        return False

    return True


def refactorDateFormat(dateFullString):
    # replace the / . with -
    dateFullString = dateFullString.replace("/", "-")
    dateFullString = dateFullString.replace(".", "-")
    dateFullString = dateFullString.replace(" ", "-")

    return dateFullString + "T00:00:00.000"


def checkDateOrder(startDate, endDate):
    if startDate is None or endDate is None:
        return False

    if startDate > endDate:
        return False

    return True


def identifyWichAPICall(args):
    if args.keyword is not None:
        return "keyword"
    elif args.vendor is not None or args.product is not None:
        return "vendorProduct"
    else:
        return "all"


def createVirtualMatchString(vendor, product):
    if vendor is None and product is None:
        return None

    if vendor is None:
        vendor = "*"
    if product is None:
        product = "*"

    return "cpe:2.3:*:" + vendor + ":" + product + ":*:*:*:*:*:*:*"


def printAllCveObjects(cveList):
    for i in range(len(cveList)):
        cveList[i].showAll()

    print("\n" + "Total number of CVEs: " + str(len(cveList)))
