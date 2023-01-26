import re


def checkDateFormat(dateFullString):
    if dateFullString is None:
        return None

    # regex to get the date from the string in the format of YYYY-MM-DD or YYYY/MM/DD or YYYY.MM.DD
    dateRegex = re.compile(r'^(19|20)\d\d([- /.])(0[1-9]|1[012])\2(0[1-9]|[12][0-9]|3[01])$')

    # if the date is not in the correct format return None
    if dateRegex.search(dateFullString) is None:
        return None

    return dateRegex.search(dateFullString).group()


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
