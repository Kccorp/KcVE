# get all arguments from the command line
import argparse
from functions import *


def getArgs():
    parser = argparse.ArgumentParser(description='CVE Search')
    parser.add_argument('-k', '--keyword', help='Keyword to search for', required=False)
    parser.add_argument('-s', '--startDate', help='Start date to search for', required=True)
    parser.add_argument('-e', '--endDate', help='End date to search for', required=False)

    return parser.parse_args()


def checkArgs(args):
    if checkDateFormat(args.startDate) is None:
        print("\033[91m" + "Start date is not in the correct format" + "\033[0m")
        return False

    if checkDateOrder(args.startDate, args.endDate) is False:
        print("\033[91m" + "Start date is after end date" + "\033[0m")
        return False

    if checkDateFormat(args.endDate) is None:
        print("\033[91m" + "End date is not in the correct format" + "\033[0m")
        return False

    return True
