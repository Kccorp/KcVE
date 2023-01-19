# importing the requests library


from cveClass import *
from request import *


def main():
    data = callApiAll()

    cveList = []
    cpeList = []

    for i in range(len(data['vulnerabilities'])):
        cve = Cve(data['vulnerabilities'][i]['cve']['id'],
                  data['vulnerabilities'][i]['cve']['published'],
                  data['vulnerabilities'][i]['cve']['lastModified'],
                  data['vulnerabilities'][i]['cve']['descriptions'][0]['value'])

        cve.getCvss(data['vulnerabilities'][i]['cve']['metrics']['cvssMetricV31'][0]['cvssData']['version'],
                    data['vulnerabilities'][i]['cve']['metrics']['cvssMetricV31'][0]['cvssData']['baseScore'],
                    data['vulnerabilities'][i]['cve']['metrics']['cvssMetricV31'][0]['cvssData']['vectorString'],
                    data['vulnerabilities'][i]['cve']['metrics']['cvssMetricV31'][0]['exploitabilityScore'])

        for j in range(len(data['vulnerabilities'][i]['cve']['configurations'][0]['nodes'][0]['cpeMatch'])):
            cpe = data['vulnerabilities'][i]['cve']['configurations'][0]['nodes'][0]['cpeMatch'][j][
                'criteria'].split(":")
            cpeObject = Cpe(cpe[3], cpe[4], cpe[5])
            cpeList.append(cpeObject)

        cve.getCpe(cpeList)
        cveList.append(cve)

        cpeList = []





    for i in range(len(cveList)):
        cveList[i].showAll()


if __name__ == '__main__':
    main()
