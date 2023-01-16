# importing the requests library


from cveClass import *
from request import *


def main():
    data = callApiAll()

    cveList = []
    for i in range(len(data['vulnerabilities'])):
        cve = Cve(data['vulnerabilities'][i]['cve']['id'],
                  data['vulnerabilities'][i]['cve']['published'],
                  data['vulnerabilities'][i]['cve']['lastModified'],
                  data['vulnerabilities'][i]['cve']['descriptions'][0]['value'])

        print(data['vulnerabilities'][i]['cve']['id'],
                  data['vulnerabilities'][i]['cve']['published'],
                  data['vulnerabilities'][i]['cve']['lastModified'],
                  data['vulnerabilities'][i]['cve']['descriptions'][0]['value'])

        cveList.append(cve)

    print("\n"+str(cveList))


if __name__ == '__main__':
    main()
