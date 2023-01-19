from cpeClass import Cpe
from cveClass import Cve

def parseCpe(cpeList):
    cpeList = cpeList['vulnerabilities'][0]['cve']['configurations'][0]['nodes'][0]['cpeMatch']
    cpeList = cpeList[0]['cpe23Uri'].split(":")
    cpe = Cpe(cpeList[3], cpeList[4], cpeList[5])
    return cpe