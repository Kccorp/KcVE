# importing the requests library


from cveClass import *
from request import *


def main():

    data = callApiAll()

    cveList = []
    for i in range(len(data['vulnerabilities'])):
        cve = []

        print(data['vulnerabilities'][i]['cve']['id'])
        cveId.append(data['vulnerabilities'][i]['cve']['id'])


    print(cveId)


if __name__ == '__main__':
    main()