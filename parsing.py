from cpeClass import Cpe
from cveClass import Cve


def parseAllCpeIntoList(data, cpeList, i):
    for j in range(len(data['vulnerabilities'][i]['cve']['configurations'][0]['nodes'][0]['cpeMatch'])):
        cpe = data['vulnerabilities'][i]['cve']['configurations'][0]['nodes'][0]['cpeMatch'][j][
            'criteria'].split(":")
        cpeObject = Cpe(cpe[3], cpe[4], cpe[5])
        cpeList.append(cpeObject)

    return cpeList


def parseDataToCve(data):
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

        cve.getSource(data['vulnerabilities'][i]['cve']['references'][0]['source'],
                      data['vulnerabilities'][i]['cve']['references'][0]['url'])

        cpeList = parseAllCpeIntoList(data, cpeList, i)

        cve.getCpe(cpeList)
        cveList.append(cve)

        cpeList = []

    return cveList
