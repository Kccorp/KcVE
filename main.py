from request import *
from parsing import *


def main():
    data = callApiAll()

    cveList = parseDataToCve(data)

    for i in range(len(cveList)):
        cveList[i].showAll()


if __name__ == '__main__':
    main()
