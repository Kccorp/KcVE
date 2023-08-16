# get all arguments from the command line
from functions import *

import argparse
import os
import time
from datetime import datetime, timedelta


def getArgs():
    parser = argparse.ArgumentParser(description='CVE Search')
    parser.add_argument('-k', '--keyword', help='Keyword to search for', required=False)
    parser.add_argument('-s', '--startDate', help='Start date to search for', required=False)
    parser.add_argument('-e', '--endDate', help='End date to search for', required=False)
    parser.add_argument('-v', '--vendor', help='Vendor to search for', required=False)
    parser.add_argument('-p', '--product', help='Product to search for', required=False)
    parser.add_argument('-w', '--output', help='Output file name', required=False)
    parser.add_argument('-t', '--time', help='The number of days to be searched', required=False)

    return parser.parse_args()


def checkArgs(args):
    if args.time is not None and (args.startDate is not None or args.endDate is not None):
        print("\033[91m" + "You can't use time and startDate/endDate at the same time" + "\033[0m")
        return False

    # check if startDate and endDate are both None and if time is None
    if args.time is None and args.startDate is None and args.endDate is None:
        currentTime = datetime.now()
        args.endDate = currentTime.strftime("%Y-%m-%d")

        args.startDate = (currentTime - timedelta(days=120)).strftime("%Y-%m-%d")

    # if args.time is not None:
        # if int(args.time) > 120:
        #     print("\033[91m" + "The research period is limited to 4 months " + "\033[0m")
        #     return False
        # elif int(args.time) < 0:
        #     print("\033[91m" + "The research period can't be negative " + "\033[0m")
        #     return False

    if args.time is not None:
        currentTime = datetime.now()
        args.endDate = currentTime.strftime("%Y-%m-%d")
        args.startDate = (currentTime - timedelta(days=int(args.time))).strftime("%Y-%m-%d")

    if checkDateFormat(args.startDate) is None:
        print("\033[91m" + "Start date is not in the correct format (ex.YYYY/MM/DD)" + "\033[0m")
        return False

    if checkDateOrder(args.startDate, args.endDate) is False:
        print("\033[91m" + "Start date is after end date" + "\033[0m")
        return False

    if checkDateFormat(args.endDate) is None:
        print("\033[91m" + "End date is not in the correct format (ex.YYYY/MM/DD)" + "\033[0m")
        return False

    if args.keyword is not None and (args.vendor is not None or args.product is not None):
        print("\033[91m" + "You can't use -k with -v or -p" + "\033[0m")
        return False

    # check if args.keyword has no symbols
    if args.keyword is not None:
        if not args.keyword.isalnum():
            print("\033[91m" + "Keyword can't contain symbols" + "\033[0m")
            return False

    # check if args.vendor has no symbols
    if args.vendor is not None:
        if not args.vendor.isalnum():
            print("\033[91m" + "Vendor can't contain symbols" + "\033[0m")
            return False

    # check if args.product has no symbols
    if args.product is not None:
        if not args.product.isalnum():
            print("\033[91m" + "Product can't contain symbols" + "\033[0m")
            return False

    # if -w is used, verify if end of str is .html
    if args.output is not None:
        if args.output[-5:] != ".html":
            args.output += ".html"

        args.output = "results/" + args.output

        if not os.path.exists("results"):
            os.makedirs("results")

    return True
